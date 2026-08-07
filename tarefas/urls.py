from django.urls import path
from .views import lista_tarefas, criar_tarefa, editar_tarefa, excluir_tarefa

urlpatterns = [
    path('', lista_tarefas, name='lista_tarefas'),
    path('criar/', criar_tarefa, name='criar_tarefa'),
    path('editar/<int:tarefa_id>/', editar_tarefa, name='editar_tarefa'),
    path('excluir/<int:tarefa_id>/', excluir_tarefa, name='excluir_tarefa'),
]