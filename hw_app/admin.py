from django.contrib import admin
from .models import *


class UseAdmin(admin.ModelAdmin):
    """Список клиентов"""
    list_display = ['name', 'mobile', 'email']
    ordering = ['name', '-reg_day']
    list_filter = ['name']
    search_fields = ['mobile', 'us_adrs']
    search_help_text = 'Поиск по телефону и адресу'


class ProductAdmin(admin.ModelAdmin):
    """Список товаров"""
    list_display = ['add_day', 'name', 'price', 'count']
    ordering = ['name', '-add_day']
    list_filter = ['price', 'count']
    search_fields = ['name', 'content']
    search_help_text = 'Поиск по имени и описанию'


class OrderAdmin(admin.ModelAdmin):
    """Список заказов"""
    list_display = ['order_day', 'us_name', 'sum_price']
    ordering = ['order_day', '-sum_price']
    list_filter = ['us_name', 'products']
    search_fields = ['order_day']
    search_help_text = 'Поиск по дате формата yyyy-mm-dd'


admin.site.register(User, UseAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
