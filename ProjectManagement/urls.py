from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('home/', view = home , name='mainHome'),
    path('', view = home , name='home')

]