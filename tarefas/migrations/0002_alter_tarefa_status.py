# Generated by Django 5.1.2 on 2024-10-25 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='status',
            field=models.CharField(choices=[('feito', 'Feito'), ('em andamento', 'Em andamento'), ('não iniciado', 'Não iniciado')], max_length=20),
        ),
    ]
