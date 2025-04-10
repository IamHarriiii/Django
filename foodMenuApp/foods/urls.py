from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('hello/', views.GreetUser, name='greet'),
    path('items/',views.items,name='items'),
    path('view/<int:item_id>',views.detailedView,name='dView'),
]
