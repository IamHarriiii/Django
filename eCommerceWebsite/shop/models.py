from django.db import models
from decimal import Decimal
# Create your models here.

CATEGORY_CHOICES = [
    ('electronics', 'Electronics'),
    ('clothing', 'Clothing'),
    ('footwear', 'Footwear'),
    ('accessories', 'Accessories'),
    ('home_appliances', 'Home Appliances'),
    ('furniture', 'Furniture'),
    ('beauty', 'Beauty & Personal Care'),
    ('groceries', 'Groceries'),
    ('books', 'Books'),
    ('stationery', 'Stationery & Office Supplies'),
    ('toys', 'Toys & Games'),
    ('sports', 'Sports & Fitness'),
    ('automotive', 'Automotive'),
    ('jewelry', 'Jewelry'),
    ('healthcare', 'Healthcare & Wellness'),
    ('baby', 'Baby Products'),
    ('pet', 'Pet Supplies'),
    ('tools', 'Tools & Hardware'),
    ('music', 'Musical Instruments'),
    ('art', 'Art & Craft'),
    ('garden', 'Gardening & Outdoors'),
    ('software', 'Software'),
    ('gaming', 'Gaming'),
    ('watches', 'Watches'),
    ('bags', 'Bags & Luggage'),
    ('mobile_accessories', 'Mobile Accessories'),
    ('kitchen', 'Kitchenware'),
    ('lighting', 'Lighting & Fixtures'),
    ('cleaning', 'Cleaning & Household'),
    ('decor', 'Home Decor'),
]

class Products(models.Model):
    product_title = models.CharField(max_length=25)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    product_DiscPrice = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    product_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    product_description = models.TextField(max_length=500)
    product_image = models.CharField(max_length=300)

    @property
    def discount_percent(self):
        if self.product_price > 0:
            return round(100 * (self.product_price - self.product_DiscPrice) / self.product_price, 2)
        return 0

    def __str__(self):
        return self.product_title