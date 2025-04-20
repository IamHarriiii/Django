from django.shortcuts import render
from . models import Products
# Create your views here.

def index(request):
   itemName = request.GET.get('search')
   if itemName:
      product_objs = Products.objects.filter(product_title__icontains=itemName)
   else:
      product_objs = Products.objects.all()
   context = {
      'product_objs': product_objs,
   }
   return render(request, 'index.html', context=context)