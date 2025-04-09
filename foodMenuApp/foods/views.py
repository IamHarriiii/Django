from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from foods.models import Items

def GreetUser(request):
    obj1 = Items.objects.all()
    template = loader.get_template('index.html')
    context = {
        'item_list' : obj1,
    }
    return render(request,'index.html',context)

def items(request):
    return HttpResponse("this is a items view")


def detailedView(request,item_id):
    item = Items.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request,'detail.html',context)