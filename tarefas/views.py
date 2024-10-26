from django.shortcuts import redirect, render
from tarefas.forms import TarefaForm
from tarefas.models import Tarefa


def tarefa_create(request):
    tarefa_id = None
    if request.method == 'POST':
        form = TarefaForm(request.POST) # Cria um formulário preenchido com os dados do tarefa
        if form.is_valid():
            tarefa = form.save()
            tarefa_id = tarefa.id # Obtém o ID da tarefa
            return redirect('home')  # Substitua 'home' pela URL desejada
    else:
        form = TarefaForm()  # Cria um formulário em branco
        
    context = {'form': form}
    if tarefa_id is not None:
        context['tarefa_id'] = tarefa_id
    
    return render(request, 'tarefa_form.html', context)


def tarefa_detalhe(request, id):
    tarefa = Tarefa.objects.get(id=id)  # Obtém o tarefa com o ID fornecido
    return render(request, 'tarefa_detalhe.html', {'tarefa': tarefa})


def tarefa_delete(request, id):
    tarefa = Tarefa.objects.get(id=id)  # Obtém o tarefa ou retorna 404 se não encontrado
    if request.method == 'POST':
        tarefa.delete()  # Deleta o tarefa
        return redirect('home')  # Redireciona para a página de listagem de tarefas
    return render(request, 'tarefa_delete.html', {'tarefa': tarefa})


def tarefa_update(request, id):
    tarefa = Tarefa.objects.get(id=id)  # Obtém o tarefa ou retorna 404 se não encontrado
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa) # Cria um formulário preenchido com os dados do tarefa
        if form.is_valid():
            form.save()  # Salva o tarefa
            return redirect('home')  # Redireciona para a página de listagem de tarefas
    else:
        form = TarefaForm(instance=tarefa)  # Cria um formulário preenchido com os dados do tarefa
        
    return render(request, 'tarefa_form.html', {'form': form})  # Renderiza o template com o formulário