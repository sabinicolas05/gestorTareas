from django.urls import path 
from .views import *

urlpatterns = [
    path('adjuntar', adjuntar, name='adjuntar'),
    path('', listar, name='listar')]
