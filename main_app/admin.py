from django.contrib import admin
from .models import Product, Order, Review, OrderItem

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(OrderItem)


