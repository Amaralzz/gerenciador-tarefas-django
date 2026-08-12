from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def lista_tarefas(request):
    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})

@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            nova_tererfa = form.save(commit=False)
            nova_tererfa.usuario = request.user
            nova_tererfa.save()
            return redirect('lista_tarefas')
    else: 
        form = TarefaForm()
    return render(request, 'tarefas/criar.html', {'form' : form})

@login_required
def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, usuario=request.user)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')

    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/editar.html', {'form' : form})

@login_required
def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, usuario=request.user)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')
    else:
        return redirect('lista_tarefas')

@login_required
def estatisticas(request):
    concluidas = Tarefa.objects.filter(usuario=request.user, concluida=True).count()
    pendentes = Tarefa.objects.filter(usuario=request.user, concluida=False).count()
    total = concluidas + pendentes
    return render(request, 'tarefas/estatisticas.html', {'total': total, 'concluidas': concluidas,'pendentes':pendentes})