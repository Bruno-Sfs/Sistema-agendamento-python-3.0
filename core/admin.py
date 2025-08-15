# core/admin.py

from django.contrib import admin
from .models import Cliente, Servico, Agendamento

# Registra os modelos para que apareçam na interface de admin
admin.site.register(Cliente)
admin.site.register(Servico)
admin.site.register(Agendamento)