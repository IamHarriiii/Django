from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator

def index(request):
    # Get search parameter
    itemName = request.GET.get('search')
    
    #Search Code
    if itemName:
        product_list = Products.objects.filter(product_title__icontains=itemName)
    else:
        product_list = Products.objects.all()
    
    product_list = product_list.order_by('id')
    
    # Paginator Code
    paginator = Paginator(product_list, per_page=4)
    pageNum = request.GET.get('page')
    product_objs = paginator.get_page(pageNum)
    
    context = {
        'product_objs': product_objs,
        'paginator': paginator,
    }
    
    return render(request, 'index.html', context=context)