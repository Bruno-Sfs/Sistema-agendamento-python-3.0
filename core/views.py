# core/views.py

from django.shortcuts import render
from .models import Agendamento  # 1. Importe o modelo Agendamento

def home(request):
    # 2. Busque todos os objetos Agendamento do banco de dados
    agendamentos = Agendamento.objects.order_by('data_hora') # Ordena pelos mais próximos

    # 3. Envie os dados para o template através de um "dicionário de contexto"
    return render(request, 'core/index.html', {'agendamentos': agendamentos})
