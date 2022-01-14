from django.urls import path
from . import views


urlpatterns = [
    path('', views.Asda_scrape, name='webscraper-home'),
    ]
