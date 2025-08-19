# core/urls.py

from django.urls import path
from . import views  # É AQUI que importamos as views

urlpatterns = [
    path('', views.home, name='home'), # E aqui nós usamos a view 'home'
]