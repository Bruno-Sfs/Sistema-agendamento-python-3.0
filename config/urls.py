# config/urls.py

from django.contrib import admin
from django.urls import path, include  # Precisa do 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),   # A única função dele é incluir as URLs do app 'core'
]