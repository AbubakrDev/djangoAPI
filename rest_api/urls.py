from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('home/', home , name='home'),
    path('krosovkaMakeAPI/', krosovkaMakeAPI, name='krosovkaMakeAPI')
]
