from django.urls import path
from . import views


urlpatterns = [
    path('asdascrape', views.Asda_scrape, name='scrape-asda'),
    path('', views.Home_view.as_view(), name='webscraper-home'),
    ]
