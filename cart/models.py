from django.db import models
from django.core.validators import MinValueValidator
from user.models import User
from product.models import Product
from order.models import Order, OrderLine
import logging

logger = logging.getLogger(__name__)

# Create your models here.
class Cart(models.Model):
    OPEN = 10
    SUBMITTED = 20
    STATUSES = (
        (OPEN, 'Open'), (SUBMITTED, 'Submitted'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE,
        null=True, blank=True, related_name='cart')
    status = models.IntegerField(choices=STATUSES, default=OPEN)

    def is_empty(self):
        return self.cart_item.all().count() == 0

    def count(self):
        return sum(i.quantity for i in self.cart_item.all())

    def create_order(self, billing_address, shipping_address):
        if not self.user:
            raise 'Cannot create order without user'
        logger.info(
            "Creating order for cart_id: %d"
            ", shipping_address_id: %d, billing_address_id: %d",
            self.id, billing_address.id, shipping_address.id
        )
        order_data = {
            'user':                 self.user,
            'billing_name':         billing_address.name,
            # 'billing_contact':      billing_address.contact,
            'billing_address1':     billing_address.address1,
            'billing_address2':     billing_address.address2,
            'billing_city':         billing_address.city,
            'billing_zipcode':      billing_address.zipcode,
            'billing_state':        billing_address.state,
            'billing_country':      billing_address.country,
            'shipping_name':        shipping_address.name,
            # 'shipping_contact':     shipping_address.contact,
            'shipping_address1':    shipping_address.address1,
            'shipping_address2':    shipping_address.address2,
            'shipping_city':        shipping_address.city,
            'shipping_zipcode':     shipping_address.zipcode,
            'shipping_state':       shipping_address.state,
            'shipping_country':     shipping_address.country
        }
        order = Order.objects.create(**order_data)
        c = 0
        for line in self.cart_item.all():
            for item in range(line.quantity):
                order_line_data = {
                    'order': order,
                    'product': line.product,
                    'vendor': line.product.vendor,
                }
                order_line = OrderLine.objects.create(**order_line_data)
                c += 1
        logger.info('Created order with id=%d and lines_count=%d', order.id, c)
        self.status = Cart.SUBMITTED
        self.save()
        return order

class CartLine(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
