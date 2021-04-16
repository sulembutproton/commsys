from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.utils.text import slugify
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/product_list.html', context)

def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)

def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            product = form.save(commit=False)
            product.slug = slugify(name)
            product.vendor = request.user
            product.save()
            logger.info('{} is created new product: {}'.format(request.user, name))
            return redirect('user:vendor')
    context = {'form': form}
    return render(request, 'product/product_create.html', context)

def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            name = form.cleaned_data['name']
            product = form.save(commit=False)
            product.slug = slugify(name)
            product.vendor = request.user
            product.save()
            form.save()
            logger.info('{} is updated the product: {}'.format(request.user, name))
            return redirect('user:vendor')
    context = {'form': form}
    return render(request, 'product/product_update.html', context)

def product_delete(request, id):
    context = {}
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        logger.info('{} has deleted product: {}'.format(request.user, product))
        return redirect('user:vendor')
        context = {'product': product}
    return render(request, 'product/product_delete.html', context)
