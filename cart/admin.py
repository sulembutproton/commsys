from django.contrib import admin
from .models import Cart, CartLine


# Register your models here.
class CartLineInline(admin.TabularInline):
    model = CartLine
    raw_id_fields = ('product', )

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'status', 'count'
    )
    list_editable = ('status', )
    list_filter = ('status', )
    inlines = [CartLineInline, ]
