from django.shortcuts import render
from . models import Products
# Create your views here.

def index(request):
    product_objs = Products.objects.all()
    context ={
       'product_objs' : product_objs, 
    }
    return render(request,'index.html',context=context)