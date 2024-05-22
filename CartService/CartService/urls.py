"""CartService URL Configuration

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
    path('', views.allCart, name="cart"),
    path('add/<slug:slug>', views.add, name="add-cart"),
    path('add_mobile/<slug:slug>', views.addMobile, name="add-mobile-to-cart"),
    path('add_clothes/<slug:slug>', views.addClothes, name="add-clothes-to-cart"),
    path('delete/<slug:slug>', views.delete, name="delete-cart"),
    path('update', views.update, name='update-cart'),
    # api cart
    path('api/cart/<int:user_id>/<slug:product_slug>', service.get_and_update_cart),
    path('api/<int:user_id>/<slug:product_slug>/delete', service.delete_cart),
    path('api/<int:user_id>/create', service.get_carts_and_create_cart),
]
