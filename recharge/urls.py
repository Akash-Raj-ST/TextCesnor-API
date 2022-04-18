from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recharge),
    path('getbalance/<str:username>', views.get_balance)
]
