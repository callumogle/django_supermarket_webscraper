from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView

from time import strftime

from .tasks import webscraper
from .models import Asdascrape
from .forms import SearchForm
# Create your views here.

class Home_view(View):
    def get(self,request):
        
        # taken and modified from ron_g https://stackoverflow.com/questions/20555673/django-query-get-last-n-records
        last_fifty = Asdascrape.objects.filter().order_by('-id')[:50:-1]
        context = {"context" : last_fifty}
        return render(request,'webscraper/displayresults.html', context)

# calls an instance of the form and passes into the search template
def Get_search(request):
    # dont forsee an instance of using POST with this form but still
    if request.method == 'POST':
        pass
    else:
        form = SearchForm()
    return render(request, 'webscraper/search.html',{'form':form})

def Asda_scrape(request):
    # definetly can do this better
    if request.GET.get('item_to_search', None):
        todays_date = strftime("%Y-%m-%d")
        search_query = Asdascrape.objects.filter(item_searched=request.GET['item_to_search'], date_searched=todays_date)
        if search_query.count() > 0:
            context = {"context" : search_query}
        else:
            webscraper(request.GET['item_to_search'])
            context = Asdascrape.objects.filter(item_searched=request.GET['item_to_search'], date_searched=todays_date)
            context = {"context":context}

        return render(request,'webscraper/displayresults.html', context)
    else:
        return HttpResponse("<div>goodbye</div>")
    
    
class ItemDetailView(DetailView):
    model = Asdascrape
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("hello",self.kwargs['pk'])
        precontext = Asdascrape.objects.filter(pk=self.kwargs['pk'])[0]
        context['item_history'] = Asdascrape.objects.filter(item_name=precontext)
        return context

def Item_view(request):
    context = Asdascrape.objects.filter(item_name=request.GET.get('item_name'))

    return render(request,'webscraper/asdascrape_detail.html',context)