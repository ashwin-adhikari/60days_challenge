from django.urls import path
from . import views

urlpatterns = [
    
path('',views.index,name='index'),
#in views.index .index is the name of the function called in views.py name is like id
path('counter',views.counter, name='counter')
]
