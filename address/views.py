from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Address
from .forms import AddressForm, AddressSelectionForm
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cart.models import Cart
import logging

logger = logging.getLogger(__name__)

# Create your views here.
@login_required(login_url=('user:login'))
def address_list(request):
    addresses = Address.objects.filter(user=request.user)
    context = {'addresses': addresses}
    return render(request, 'address/address_list.html', context)

@login_required(login_url=('user:login'))
def address_create(request):
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            logger.info('{} created a new address'.format(request.user))
            return redirect('address:address_list')
    context = {'form': form}
    return render(request, 'address/address_create.html', context)

@login_required(login_url=('user:login'))
def address_update(request, id):
    address = get_object_or_404(Address, id=id)
    form = AddressForm(instance=address)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            logger.info('{} updated their address with id: {}'.format(request.user, address.id))
            return redirect('address:address_list')
    context = {'form': form}
    return render(request, 'address/address_update.html', context)

@login_required(login_url=('user:login'))
def address_delete(request, id):
    address = get_object_or_404(Address, id=id)
    if request.method == 'POST':
        address.delete()
        logger.info('{} has deleted his address with Address: {}'.format(request.user, address))
        return redirect('address:address_list')
    context = {'address': address}
    return render(request, 'address/address_delete.html', context)

class AddressSelectionView(FormView):
    template_name = 'address/address_select.html'
    form_class = AddressSelectionForm
    success_url = reverse_lazy('order:checkout_done')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        del self.request.session['cart_id']
        cart = self.request.cart
        cart.create_order(
            form.cleaned_data['billing_address'],
            form.cleaned_data['shipping_address']
        )
        return super().form_valid(form)
