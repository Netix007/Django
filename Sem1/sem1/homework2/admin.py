from django.contrib import admin
from .models import Client, Item, Order


admin.site.register(Client)
admin.site.register(Item)
admin.site.register(Order)
