from django.contrib import admin
from .models import Autor, Livro, Emprestimo

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento')
    search_fields = ('nome',)  # Campo de pesquisa por nome
    list_filter = ('data_nascimento',)  # Filtro por data de nascimento


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao', 'disponivel')
    search_fields = ('titulo', 'autor__nome')  # Pesquisa por título e autor
    list_filter = ('data_publicacao', 'disponivel', 'autor')  # Filtros adicionais
    ordering = ('-data_publicacao',)  # Ordenação padrão


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'nome_usuario', 'data_emprestimo', 'data_devolucao')
    search_fields = ('nome_usuario', 'livro__titulo')  # Pesquisa por usuário e livro
    list_filter = ('data_emprestimo', 'data_devolucao', 'livro__autor')  # Filtros avançados
