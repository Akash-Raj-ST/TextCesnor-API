from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('level1/', views.text_censor_level1),
    path('level2/', views.text_censor_level2),
    path('level3/', views.text_censor_level3),

]
