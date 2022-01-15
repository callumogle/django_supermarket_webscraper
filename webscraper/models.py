from django.db import models
from django.utils import timezone
# Create your models here.
class Asdascrape(models.Model):
    store = models.CharField(max_length=15)
    item_name = models.CharField(max_length=50)
    item_image = models.CharField(max_length=55)
    item_price = models.DecimalField(max_digits=8, decimal_places=2)
    unit_price = models.CharField(max_length=20) 
    item_searched = models.CharField(max_length=50)
    date_searched = models.DateField(default=timezone.now)
    item_url = models.CharField(max_length=75)

    def __str__(self):
        return self.item_name