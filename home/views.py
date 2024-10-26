from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projetos.models import Projeto
from tarefas.models import Tarefa

@login_required
def homeView(request):
    projetos = Projeto.objects.all() # Obtém todos os projetos
    tarefas = Tarefa.objects.all()
    return render(request, 'home.html', {'projetos': projetos, 'tarefas': tarefas})