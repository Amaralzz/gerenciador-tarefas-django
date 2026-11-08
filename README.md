# Gerenciador de Tarefas

Aplicação web em Django para organizar tarefas pessoais. Cada usuário entra com sua conta, cria e acompanha as próprias tarefas e vê um resumo do que está concluído e pendente.

## Funcionalidades

- Login/logout com contas criadas pelo admin do Django
- CRUD completo de tarefas (criar, listar, editar, excluir)
- Página de estatísticas com total, concluídas e pendentes
- Isolamento por usuário: cada conta só acessa as próprias tarefas

## Tecnologias

- Python / Django
- SQLite
- HTML / CSS

## Como rodar localmente

Requer Python 3.12 ou superior.

```bash
git clone https://github.com/Amaralzz/gerenciador-tarefas-django.git
cd gerenciador-tarefas-django

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/tarefas/` e entre com o usuário criado.

## Decisões técnicas

- **Isolamento de dados por usuário**: as consultas filtram por `usuario=request.user`, e editar ou excluir usa `get_object_or_404(Tarefa, id=tarefa_id, usuario=request.user)`. Assim, trocar o ID na URL não dá acesso à tarefa de outra pessoa.
- **Exclusão só por POST**: a view de excluir ignora requisições GET, então um simples link não apaga dados.
- **Chave secreta fora do código**: em produção, a `SECRET_KEY` vem da variável de ambiente `DJANGO_SECRET_KEY`.

## Possíveis melhorias

- Cadastro de usuários pela própria aplicação
- Filtros por status e prazo nas tarefas
- Testes automatizados das views
