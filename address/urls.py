from django.urls import path
from . import views

app_name = 'address'

urlpatterns = [
    path('address_list/', views.address_list, name='address_list'),
    path('address_create/', views.address_create, name='address_create'),
    path('address_list/<int:id>/', views.address_update, name='address_update'),
    path('address_list/<int:id>/delete/', views.address_delete, name='address_delete'),
    path('address_select/', views.AddressSelectionView.as_view(), name='address_select'),
]
