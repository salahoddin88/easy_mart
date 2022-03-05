from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart', views.AddToCartView.as_view(), name="AddToCartView"),
    path('cart', views.CartView.as_view(), name="CartView"),
    path('checkout', views.CheckoutView.as_view(), name="CheckoutView"),
]
