from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'vendor', 'price', 'available'
    )
    list_filter = (
        'available',
    )
    search_fields = (
        'name', 'vendor'
    )
    prepopulated_fields = {
        'slug': ('name', )
    }
    ordering = ('name', )
