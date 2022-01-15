from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Asdascrape

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from time import sleep, strftime
from random import randint
import requests
import os

from webdriver_manager.chrome import ChromeDriverManager


# Create your views here.

class MyView(View):
    def get(self,request):
        return render(request,'webscraper/home.html')

def grab_image(element, image_css):
    image = element.select_one(image_css)
    try:

        link = image['src']
    except KeyError as e:
        print("really should be finding the images, probably some dumb thing")
        print(e)
        return "N/A"

    try:
        img_name = image['alt']
        img_name = img_name.replace("\r", "").replace(
        ' ', '-').replace('/', '') + ".jpg"
    except KeyError as e:
        print(e)
        img_name = "N/A"
    

    if os.path.isfile(f"{os.getcwd()}/webscraper/static/webscraper/asda/{img_name}"):
        print(f"file: {img_name} already exists")
    else:
        with open(f"{os.getcwd()}/webscraper/static/webscraper/asda/{img_name}", 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', img_name)
    return img_name

def Asda_scrape(request):
    
    option = webdriver.ChromeOptions()
    # makes chrome incognito so no cookies affect search result
    option.add_argument("incognito")
    # open chrome without displaying it to the user
    option.add_argument("--headless")
    # open website in fullscreen
    option.add_argument("--start-maximized")
    # adding a user agent reduces chances of detection.
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    option.add_argument(f'user-agent={user_agent}')
    service = Service(executable_path=ChromeDriverManager().install())
    results=[]
    with webdriver.Chrome(service=service, options = option) as driver:
        url = "https://groceries.asda.com/search/apples"
        driver.get(url)
        last_height = driver.execute_script("return document.body.scrollHeight")
        # scroll down the webpage, loading in images.
        while True:
            sleep(1)
            rand_y = randint(750, 1000)
            driver.execute_script(f"window.scrollBy(0, {rand_y});")
            new_height = driver.execute_script("return window.pageYOffset")
            print(new_height)
            if new_height == last_height:
                break
            else:
                last_height = new_height

        html = driver.page_source
        soup = bs(html, 'html.parser')
        main = soup.select_one("ul.co-product-list__main-cntr")
        # why the fuck does this still catch the stuff at the bottom
        items = main.select("li.co-item")

        for elem in items:
            img_name = grab_image(elem,'img.co-item__image')
            
            try:
                name = elem.select_one('a.co-product__anchor').text
            except NoSuchElementException:
                name = "n/a"
            try:
                price = elem.select_one('strong.co-product__price').text
                # remove formating from prices to allow them to go into database
                price = price.replace("£", '')
                price = price.replace("now", '')
                price = price.strip()
            except (NoSuchElementException, AttributeError) as e:
                price = None
            try:
                unit_price = elem.select_one(
                    'span.co-product__price-per-uom').text
            except (NoSuchElementException, AttributeError) as e:
                unit_price = "n/a"

            # inserts data into sql database using the model
            Asdascrape.objects.create(
                                    store='Asda', item_name=name,
                                    item_image=img_name,
                                    item_price=price, unit_price=unit_price, 
                                    item_searched='apples', item_url= driver.current_url
                                    )
    print("script ended")
    return render(request,'webscraper/home.html')
