from django.urls import path
from django.views.generic import TemplateView

app_name ='order'

urlpatterns = [
    path('order/done/', TemplateView.as_view(template_name='order/order_done.html'), name='checkout_done'),
]
