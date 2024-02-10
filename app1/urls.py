from django.contrib import admin
from django.urls import path

from app1.views import *


urlpatterns = [

    path('home/',home,name='home'),
]
