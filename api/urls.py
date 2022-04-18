from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('level1/<str:api_key>', views.text_censor_level1),
    path('level2/<str:api_key>', views.text_censor_level2),
    path('level3/<str:api_key>', views.text_censor_level3),

]
