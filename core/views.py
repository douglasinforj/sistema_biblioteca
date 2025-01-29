from django.shortcuts import render
from .models import Livro, Autor, Emprestimo
from django.db.models import Q

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

    return render(request, 'core/livros_list.html', {'livros': livros})

