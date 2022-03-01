from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name="LoginView"),
    path('logout', views.LogoutView, name="LogoutView"),
]
