from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('home/', home , name='home'),
    path('krosovka-api/', krosovkaMakeAPI),
    path('krosovka-api/<int:pk>/', singleAPI),
    path('create/', malumotJoylash),
    path('create/<int:pk>/', malumotUpdate),
]
