from django.contrib import admin
from django.urls import path

from app.views import *


urlpatterns = [
    path('base/',base,name='base'),
    path('home/',home,name='home'),
]
