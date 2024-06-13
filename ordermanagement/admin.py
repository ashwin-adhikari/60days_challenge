from django.contrib import admin
from .models import Table, Order, Payment, Item, Manager

# Register your models here.
admin.site.register(Table),
admin.site.register(Order),
admin.site.register(Payment),
admin.site.register(Manager),
admin.site.register(Item),