from django.contrib import admin
from .models import Product,Order,Reviews,ShipingAddress,OrderItem
# Register your models here.
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(ShipingAddress)
admin.site.register(Reviews)