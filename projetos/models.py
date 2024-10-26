from django.db import models

class Projeto(models.Model):
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
    gerente_responsavel = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome