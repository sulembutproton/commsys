from django.contrib.auth.signals import user_logged_in
from .models import Cart
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)

@receiver(user_logged_in)
def merge_baskets_if_found(sender, user, request, **kwargs):
    anonymous_cart = getattr(request, 'cart', None)
    if anonymous_cart:
        try:
            loggedin_cart = Cart.objects.get(user=user, status=Cart.OPEN)
            for item in anonymous_cart.cart_item.all():
                item.cart = loggedin_cart
                item.save()
            anonymous_cart.delete()
            request.cart = loggedin_cart
            logger.info('Merged Cart to id: %d', loggedin_cart.id)
        except Cart.DoesNotExist:
            anonymous_cart.user = user
            anonymous_cart.save()
            logger.info('Assigned {} to cart id: {}'.format(user, anonymous_cart.id))
