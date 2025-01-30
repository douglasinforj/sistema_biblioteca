from django.shortcuts import render
from .models import Livro, Autor, Emprestimo
from django.db.models import Q

from django.core.paginator import Paginator     #paginação



def home(request):
    return render(request, 'core/home.html')



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



from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Emprestimo

def emprestimos_list(request):
    usuario = request.GET.get('usuario', '')
    livro = request.GET.get('livro', '')
    data_inicio = request.GET.get('data_inicio', '')
    data_fim = request.GET.get('data_fim', '')

    emprestimos = Emprestimo.objects.all()

    if usuario:
        emprestimos = emprestimos.filter(nome_usuario__icontains=usuario)  
    if livro:
        emprestimos = emprestimos.filter(livro__titulo__icontains=livro)
    if data_inicio:
        emprestimos = emprestimos.filter(data_emprestimo__gte=data_inicio)
    if data_fim:
        emprestimos = emprestimos.filter(data_devolucao__lte=data_fim)

    # Paginação: 20 registros por página
    paginator = Paginator(emprestimos, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/emprestimos_list.html', {'emprestimos': page_obj})  # Corrigido contexto
