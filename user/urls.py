from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('vendor/', views.vendor, name='vendor'),
    path('customer/', views.customer, name='customer'),
    path('logout/', views.user_logout, name='logout'),
]
