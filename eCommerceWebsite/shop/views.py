from django.shortcuts import render
from . models import Products
# Create your views here.

def index(request):
    product_objs = Products.objects.all()
    return render(request,'index.html',product_objs)