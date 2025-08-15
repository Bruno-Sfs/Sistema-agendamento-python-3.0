# core/models.py

from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True) # Opcional

    # Esta função define como o objeto será exibido (ex: na lista de admin)
    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome_servico = models.CharField(max_length=100)
    duracao_minutos = models.IntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome_servico

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True)
    data_hora = models.DateTimeField()
    observacoes = models.TextField(blank=True, null=True) # Opcional

    def __str__(self):
        # Formata a data para um formato mais legível
        data_formatada = self.data_hora.strftime("%d/%m/%Y às %H:%M")
        return f"{self.cliente.nome} - {self.servico.nome_servico} em {data_formatada}"