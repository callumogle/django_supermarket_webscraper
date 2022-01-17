from django.db import models
from django.utils import timezone
# Create your models here.
class Asdascrape(models.Model):
    store = models.CharField(max_length=15)
    item_name = models.CharField(max_length=50)
    item_image = models.ImageField(default="default.jpg",upload_to="scrapedimages")
    item_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    unit_price = models.CharField(max_length=20, null=True) 
    item_searched = models.CharField(max_length=50)
    date_searched = models.DateField(default=timezone.now)
    item_url = models.CharField(max_length=75)

    def __str__(self):
        return self.item_name