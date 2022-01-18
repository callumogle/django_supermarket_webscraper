from telnetlib import SE
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from time import strftime

from .tasks import webscraper
from .models import Asdascrape
from .forms import SearchForm
# Create your views here.

class Home_view(View):
    def get(self,request):
        todays_date = strftime("%Y-%m-%d")
        context = {"context" : Asdascrape.objects.filter(item_searched='apples', date_searched=todays_date)}
        return render(request,'webscraper/displayresults.html', context)

def Get_search(request):
    # dont forsee an instance of using POST with this form but still
    if request.method == 'POST':
        pass
    else:
        form = SearchForm()
    return render(request, 'webscraper/search.html',{'form':form})

def Asda_scrape(request):
    
    if request.GET.get('item_to_search', None):
        webscraper(request.GET['item_to_search'])
    else:
        return HttpResponse("<div>goodbye</div>")
    return render(request,'webscraper/home.html')
