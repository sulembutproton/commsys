from django.shortcuts import render, redirect
from .models import User, UserRole
from .forms import RegistrationForm, UserRoleForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import logging
from product.models import Product
from order.models import Order, OrderLine
from cart.models import Cart, CartLine

logger = logging.getLogger(__name__)

# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        role_form = UserRoleForm(request.POST)
        if user_form.is_valid() and role_form.is_valid():
            first_name = user_form.cleaned_data.get('first_name')

            user = User.objects._create_user(
                email=user_form.cleaned_data['email'],
                first_name=first_name,
                last_name = user_form.cleaned_data['last_name'],
                password=user_form.cleaned_data['password'],
            )
            user.save()
            user_role = role_form.save(commit=False)

            user_role.user = user
            user_role.save()
            messages.success(request, 'Hi {}!, Your account is successfully created'.format(first_name))
            return redirect('user:login')
    else:
        user_form = RegistrationForm()
        role_form = UserRoleForm()

    context = {
        'user_form': user_form,
        'role_form': role_form,
    }
    return render(request, 'user/register.html', context)

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            logger.info('User: {},  with email: {} has logged in'.format(user, email))
            if user.role.role == UserRole.CUSTOMER:
                return redirect('product:product_list')
                messages.success(request, 'Welcome, {}! Good to see you!'.format(user))
            elif user.role.role == UserRole.VENDOR:
                return redirect('user:vendor')
                messages.success(request, 'Welcome, {}! Good to see you!'.format(user))
        else:
            messages.warning(request, 'Email or password is incorrect, Try again')
    context = {'messages': messages}
    return render(request, 'user/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('user:login')

def vendor(request):
    products = Product.objects.filter(vendor=request.user)
    orders = OrderLine.objects.filter(vendor=request.user)
    context = {'products': products, 'orders': orders}
    return render(request, 'user/vendor.html', context)

def customer(request):
    orders = Cart.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'user/customer.html', context)
