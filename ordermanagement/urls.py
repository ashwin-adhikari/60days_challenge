from django.urls import path
from django.contrib import admin
from ordermanagement import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('tablelist/',views.table_list),
    path('orderdetails/<int:order_id>/',views.order_detail),
    path('createorder/<int:table_id>/',views.create_order, name= 'create_order'),
    path('payment/<int:order_id>/',views.process_payment),
    path('',views.homepage),
]
