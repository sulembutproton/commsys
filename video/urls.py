from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('product_create/', views.product_create, name='product_create'),
    path('<int:id>/update/', views.product_update, name='product_update'),
    path('<int:id>/Delete/', views.product_delete, name='product_delete'),
]
