from django.contrib import admin
from .models import Cart, Customers, Product, orders
# Register your models here.
admin.site.register(Product)
admin.site.register(Customers)
admin.site.register(Cart)
admin.site.register(orders)