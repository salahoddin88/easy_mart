from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="HomeView"),
    path('product-list', views.ProductListView.as_view(), name="ProductListView"),
    path('product-list/<int:category_id>', views.ProductListView.as_view(), name="ProductListView"),
]

