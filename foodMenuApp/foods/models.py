from django.db import models

# Create your models here.
class Items(models.Model):

    def __str__(self):
        return f"{self.item_name} - Rs.{self.items_price}"
    
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=200)
    items_price = models.IntegerField()
    items_image = models.CharField(max_length=500,default='https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png')