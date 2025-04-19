from django.db import models

# Create your models here.

class Products(models.Model):
    product_title = models.CharField(max_length=25)
    product_price = models.FloatField(default=0.0)
    product_DiscPrice = models.FloatField(default=0.0)
    product_category = models.CharField(max_length=50)
    product_description = models.TextField(max_length=500)
    product_image = models.CharField(max_length=300)

    def __str__(self):
        return self.product_title