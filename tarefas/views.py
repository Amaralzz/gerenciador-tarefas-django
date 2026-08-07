from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')

    else: 
        form = TarefaForm()

    return render(request, 'tarefas/criar.html', {'form' : form})

def editar_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')

    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/editar.html', {'form' : form})

def excluir_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')
    else:
        return redirect('lista_tarefas')