from django.urls import path
from . import views


urlpatterns = [
    
    path('asdascrape', views.Asda_scrape, name='scrape_asda'),
    path('', views.Home_view.as_view(), name='webscraper_home'),
    path('search/', views.Get_search, name='item_search'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    ]
