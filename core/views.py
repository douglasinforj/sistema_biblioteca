from django.shortcuts import render
from .models import Livro, Autor, Emprestimo
from django.db.models import Q

from django.core.paginator import Paginator     #paginação

def livros_list(request):

    #filtros via query parameters
    titulo = request.GET.get('titulo', '')
    autor = request.GET.get('autor', '')
    disponivel = request.GET.get('disponivel', '')

    # Consulta avançada com filtros
    livros = Livro.objects.all()

    if titulo:
        livros = livros.filter(titulo__icontains=titulo)
    if autor:
        livros = livros.filter(autor__nome__icontains=autor)
    if disponivel.lower() == 'true':
        livros = livros.filter(disponivel=True)
    elif disponivel.lower() == 'false':
        livros = livros.filter(disponivel=False)

    #paginação: 20 livros por páginas
    paginator = Paginator(livros, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'core/livros_list.html', {'page_obj': page_obj})

