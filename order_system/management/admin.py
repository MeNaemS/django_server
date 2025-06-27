from django.contrib import admin
from .models import (
    BroadcastMessage, Cart, CartItem, Order, OrderItem,
    Product, Category, FAQ, UserSubscription
)

# Register your models here.
admin.site.register(BroadcastMessage)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(FAQ)
admin.site.register(UserSubscription)
