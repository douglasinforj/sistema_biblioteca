import os
import random
import sys
from django.utils.timezone import now, timedelta


# Voltar uma pasta para encontrar o settings correto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Configurar o ambiente do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biblioteca.settings")
import django
django.setup()

from core.models import Autor, Livro, Emprestimo

# Gerar nomes fictícios
NOMES_AUTORES = [
    "Machado de Assis", "Clarice Lispector", "Monteiro Lobato", "Cecília Meireles",
    "Carlos Drummond", "Manuel Bandeira", "João Cabral", "Guimarães Rosa",
    "Jorge Amado", "Lygia Fagundes Telles"
]

TITULOS_LIVROS = [
    "Introdução ao Django", "Python para Todos", "Algoritmos Modernos",
    "Aventuras de Programação", "O Código Limpo", "Data Science Simplificado",
    "Desenvolvimento Web Completo", "DevOps para Iniciantes", "Inteligência Artificial Hoje",
    "Redes Neurais Explicadas"
]

# Função para popular autores
def criar_autores():
    for nome in NOMES_AUTORES:
        Autor.objects.get_or_create(nome=nome, data_nascimento=f"19{random.randint(20, 80)}-01-01")
    print("Autores criados!")

# Função para popular livros
def criar_livros():
    autores = list(Autor.objects.all())
    for i in range(50):  # 50 livros no total
        titulo = f"{random.choice(TITULOS_LIVROS)} - Edição {i+1}"
        autor = random.choice(autores)
        disponivel = random.choice([True, False])
        Livro.objects.create(
            titulo=titulo,
            autor=autor,
            disponivel=disponivel,
            data_publicacao=f"20{random.randint(10, 23)}-{random.randint(1, 12):02d}-01"
        )
    print("Livros criados!")

# Função para popular empréstimos
def criar_emprestimos():
    livros = Livro.objects.filter(disponivel=False)[:50]  # Garantir que não estão disponíveis
    for i in range(100):  # 100 empréstimos no total
        livro = random.choice(livros)
        nome_usuario = f"Usuário {random.randint(1, 30)}"
        data_emprestimo = now() - timedelta(days=random.randint(1, 60))
        data_devolucao = data_emprestimo + timedelta(days=random.randint(7, 30)) if random.choice([True, False]) else None
        Emprestimo.objects.create(
            livro=livro,
            nome_usuario=nome_usuario,
            data_emprestimo=data_emprestimo,
            data_devolucao=data_devolucao
        )
    print("Empréstimos criados!")

# Rodar todas as funções
def popular_banco():
    criar_autores()
    criar_livros()
    criar_emprestimos()

if __name__ == '__main__':
    popular_banco()