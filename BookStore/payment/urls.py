from django.urls import path
from .views import *
from . import service

urlpatterns = [
    path('', paymentBank, name="payment-bank"),
    
    # api payment
    path('api/create_or_update', service.create_or_update_payment),
    path('api/get/<int:checkout_id>', service.get_payment_by_checkoutid),

]