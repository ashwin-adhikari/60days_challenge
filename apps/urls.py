from django.urls import path
from django.contrib import admin
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    
path('admin/',admin.site.urls),
path('drinklist/',views.drink_list),
# path('drinkdetail/', views.drink_detail),
path('drinkcreate/',views.drink_create),
path('addquantity/',views.add_quantity),
path('', views.homepage, name='index'),
# path('drinkapi/', views.drinkapi.as_view()),


    
# path('drinkdetails/<int:id>',views.drink_detail),
# path('drinklist/',views.drink_list),


]
urlpatterns = format_suffix_patterns(urlpatterns)
#now can use different extensions like .json with above urls