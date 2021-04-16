from django.contrib import admin
from .models import Order, OrderLine


# Register your models here.
class OrderLineInline(admin.TabularInline):
    model = OrderLine
    raw_id_fields = ('product', 'vendor')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'status',
    )
    list_editable = (
        'status',
    )
    list_filter = (
        'status', 'shipping_city', 'shipping_state', 'shipping_country', 'created',
    )
    inlines = [OrderLineInline,]
    fieldsets = (
        (None, {'fields': ('user', 'status')}),
        (
            'Billing Info',
            {
                'fields': (
                    'billing_name',
                    'billing_contact',
                    'billing_address1',
                    'billing_address2',
                    'billing_city',
                    'billing_zipcode',
                    'billing_state',
                    'billing_country',
                )
            },
        ),
        (
            'Shipping Info',
            {
                'fields': (
                    'shipping_name',
                    'shipping_contact',
                    'shipping_address1',
                    'shipping_address2',
                    'shipping_city',
                    'shipping_zipcode',
                    'shipping_state',
                    'shipping_country',
                )
            },
        ),
    )
