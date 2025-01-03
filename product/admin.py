from django.contrib import admin
from .models import Product,Cart

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'selling_price', 'discounted_price', 'category')
    search_fields = ('brand', 'name', 'category')
    list_filter = ('category',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'user')
    search_fields = ('product', 'user')
    list_filter = ('product', 'user')

