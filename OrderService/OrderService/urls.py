"""OrderService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', getOrders, name="orders"),
    path('checkout/', checkout, name="checkout"),
    path('details/<int:id>', detailsOrder, name="details-order"),
    path('cancel-order/<code>', cancelOrder, name="cancel-order"),
    path('re-order/<code>', re_Order, name="re-order"),

    # api order
    path('api/order/create', service.create_order),
    path('api/checkouts/<int:user_id>', service.get_checkouts_by_user),
    path('api/checkouts', service.get_checkouts),
    path('api/checkouts/<int:user_id>/<slug:code>/cancel', service.cancel_checkout),
    path('api/checkouts/<int:user_id>/<slug:code>/re_order', service.re_order_checkout),
    path('api/order-items/<int:checkout_id>', service.get_order_items),
    path('api/checkout/<int:checkout_id>', service.get_checkout),
    path('api/all-order-items', service.get_all_order_items),
]
