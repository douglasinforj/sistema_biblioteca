from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Autor, Emprestimo, Pessoa
from .forms import LivroForm, PessoaForm
from django.db.models import Q

from django.core.paginator import Paginator     #paginação



#=============================================HOME==========================================

def home(request):
    return render(request, 'core/home.html')



#=============================================LIVROS========================================

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
    paginator = Paginator(livros, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'core/livros_list.html', {'page_obj': page_obj})



# Criar novo livro
def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livros_list')
    else:
        form = LivroForm()
    return render(request, 'core/livro_form.html', {'form': form})

def livro_detail(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'core/livro_detail.html', {'livro': livro})


def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livro_detail', pk=pk)  # Redireciona para a página de detalhes do livro
    else:
        form = LivroForm(instance=livro)  # Exibe o formulário de edição para um livro existente

    return render(request, 'core/livro_form.html', {'form': form})



def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('livros_list')
    return render(request, 'core/livro_confirm_delete.html', {'livro': livro})



#==============================PESSOAS==========================================

def gestao_pessoa(request):
    return render(request, 'core/gestao_pessoa.html')



def pessoa_list(request):
    nome = request.GET.get('nome', '')
    cpf = request.GET.get('cpf', '')
    telefone =  request.GET.get('telefone', '')
    email = request.GET.get('email', '')

    # busca para filtragem

    pessoas = Pessoa.objects.all()

    if nome:
        pessoas = pessoas.filter(nome__icontains=nome)
    if cpf:
        pessoas = pessoas.filter(cpf__icontains=cpf)
    if telefone:
        pessoas = pessoas.filter(telefone__icontains=telefone)
    if email:
        pessoas = pessoas.filter(email_icontains=email)
    
    #paginação:
    paginator = Paginator(pessoas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/pessoa_list.html', {'page_obj': page_obj})



def pessoa_create(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pessoa_list')
    else:
        form = PessoaForm()
    return render(request, 'core/pessoa_form', {'form': form})


def pessoa_edit(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('pessoa_list')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'core/pessoa_form.html', {'form': form, 'pessoa': pessoa})


def pessoa_delete(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('pessoa_list')
    return render(request, 'core/pessoa_confirm_delete.html', {'pessoa': pessoa})





#============================================EMPRESTIMOS===================================



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
