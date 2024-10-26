from django.shortcuts import get_object_or_404, redirect, render
from projetos.forms import ProjetoForm
from projetos.models import Projeto


def projeto_create(request):
    projeto_id = None  # Inicializa projeto_id com None
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save()
            projeto_id = projeto.id
            return redirect('home')  # Substitua 'home' pela URL desejada
    else:
        form = ProjetoForm()  # Cria um formulário em branco
        
    context = {'form': form}
    if projeto_id is not None:
        context['projeto_id'] = projeto_id
    
    return render(request, 'projeto_form.html', context)  # Renderiza o template com o formulário # renderiza o template com o formulário como return


def projeto_detalhe(request, id):
    projeto = Projeto.objects.get(id=id)  # Obtém o projeto com o ID fornecido
    return render(request, 'projeto_detalhe.html', {'projeto': projeto})


def projeto_delete(request, id):
    projeto = Projeto.objects.get(id=id)  # Obtém o projeto ou retorna 404 se não encontrado
    if request.method == 'POST':
        projeto.delete()  # Deleta o projeto
        return redirect('home')  # Redireciona para a página de listagem de projetos
    return render(request, 'projeto_delete.html', {'projeto': projeto})


def projeto_update(request, id):
    projeto = Projeto.objects.get(id=id)  # Obtém o projeto ou retorna 404 se não encontrado
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto) # Cria um formulário preenchido com os dados do projeto
        if form.is_valid():
            form.save()  # Salva o projeto
            return redirect('home')  # Redireciona para a página de listagem de projetos
    else:
        form = ProjetoForm(instance=projeto)  # Cria um formulário preenchido com os dados do projeto
        
    return render(request, 'projeto_form.html', {'form': form})  # Renderiza o template com o formulário