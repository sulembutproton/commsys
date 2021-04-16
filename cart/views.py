from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from product.models import Product
from .models import Cart, CartLine
from .forms import CartLineFormset

import logging

logger = logging.getLogger(__name__)

# Create your views here.
def add_to_cart(request):
    product = get_object_or_404(Product, pk=request.GET.get('product_id'))
    cart = request.cart

    if not request.cart:
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        cart = Cart.objects.create(user=user)
        request.session['cart_id'] = cart.id
    cartline, created = CartLine.objects.get_or_create(cart=cart, product=product)
    if not created:
        cartline.quantity += 1
        cartline.save()
        logger.info('{} added the product: {} to their cart'.format(request.user, product))
    return HttpResponseRedirect(reverse('product:product_detail', args=(product.id,)))


def manage_cart(request):
    if not request.cart:
        return render(request, 'cart/cart.html', {'formset': None})

    if request.method == 'POST':
        formset = CartLineFormset(request.POST, instance=request.cart)
        if formset.is_valid():
            formset.save()
    else:
        formset = CartLineFormset(instance=request.cart)
    if request.cart.is_empty():
        return render(request, 'cart/cart.html', {'formset': None})
    return render(request, 'cart/cart.html', {'formset': formset})
