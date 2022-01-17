from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .tasks import asda_scrape, concurrentfuturestest


# Create your views here.

class Home_view(View):
    def get(self,request):
        context = {"context" : Asdascrape.objects.all()}
        return render(request,'webscraper/displayresults.html', context)



def Asda_scrape(request):
    concurrentfuturestest()
    return render(request,'webscraper/home.html')
