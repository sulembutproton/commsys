from django.db import models
from user.models import User
from product.models import Product
from user.models import User

# Create your models here.
class Order(models.Model):
    NEW = 10
    PAID = 20
    DONE = 30
    STATUSES = (
        (NEW, 'New'), (PAID, 'Paid'), (DONE, 'Done')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUSES, default=NEW)
    billing_name = models.CharField(max_length=100)
    billing_contact = models.CharField(max_length=100)
    billing_address1 = models.CharField(max_length=100)
    billing_address2 = models.CharField(max_length=100, blank=True)
    billing_city = models.CharField(max_length=100)
    billing_zipcode = models.CharField(max_length=100)
    billing_state = models.CharField(max_length=100)
    billing_country = models.CharField(max_length=100)
    shipping_name = models.CharField(max_length=100)
    shipping_contact = models.CharField(max_length=100)
    shipping_address1 = models.CharField(max_length=100)
    shipping_address2 = models.CharField(max_length=100, blank=True)
    shipping_city = models.CharField(max_length=100)
    shipping_zipcode = models.CharField(max_length=100)
    shipping_state = models.CharField(max_length=100)
    shipping_country = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def billing_address(self):
        return ", ".join([
            self.billing_name, self.billing_contact, self.billing_address1,
            self.billing_address2, self.billing_city, self.billing_zipcode,
            self.billing_state, self.billing_country
        ])

    def shipping_address(self):
        return ", ".join([
            self.shipping_name, self.shipping_contact, self.shipping_address1,
            self.shipping_address2, self.shipping_city, self.shipping_zipcode,
            self.shipping_state, self.shipping_country
        ])

class OrderLine(models.Model):
    NEW = 10
    PROCESSING = 20
    SENT = 30
    CANCELLED = 40
    STATUSES = (
        (NEW, 'New'), (PROCESSING, 'Processing'), [SENT, 'Sent'], (CANCELLED, 'Cancelled')
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='lines')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    vendor = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUSES, default=NEW)
