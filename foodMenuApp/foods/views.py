from django.shortcuts import render
from django.http import HttpResponse

from foods.models import Items

def GreetUser(request):
    obj1 = Items.objects.all()

    return HttpResponse(obj1)

def items(request):
    return HttpResponse("this is a items view")