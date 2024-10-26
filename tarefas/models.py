from django.db import models
from projetos.models import Projeto # Importa o modelo Projeto

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('feito', 'Feito'),
        ('em andamento', 'Em andamento'),
        ('não iniciado', 'Não iniciado'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_termino = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)  # Seletor de status
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas')
    responsavel = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome