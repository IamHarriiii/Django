from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.GreetUser, name='greet'),
    path('items/',views.items,name='items')
]
