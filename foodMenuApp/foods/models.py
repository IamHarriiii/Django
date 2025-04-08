from django.db import models

# Create your models here.
class Items(models.Model):

    def __str__(self):
        return f"{self.item_name} - Rs.{self.items_price}"
    
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=200)
    items_price = models.IntegerField()