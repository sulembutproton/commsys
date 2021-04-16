from django.forms import inlineformset_factory
from .models import Cart, CartLine

CartLineFormset = inlineformset_factory(
    Cart,
    CartLine,
    fields=('quantity',),
    extra=0,
)
