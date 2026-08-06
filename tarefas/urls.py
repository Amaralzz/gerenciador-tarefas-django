from django.urls import path
from .views import lista_tarefas, criar_tarefa

urlpatterns = [
    path('', lista_tarefas, name='lista_tarefas'),
    path('criar/', criar_tarefa, name='criar_tarefa'),
]