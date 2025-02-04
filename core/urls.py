from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('livros/', views.livros_list, name='livros_list'),
    path('livros/novo', views.livro_create, name='livro_create'),
    path('livros/<int:pk>/', views.livro_detail, name='livro_detail'),
    path('livros/<int:pk>/update/', views.livro_update, name='livro_update'),
    path('livros/<int:pk>/delete/', views.livro_delete, name='livro_delete'),


    path('gestao_pessoa/', views.gestao_pessoa, name='gestao_pessoa'),
    path('pessoa/', views.pessoa_list, name='pessoa_list'),
    path('pessoa/novo/', views.pessoa_create, name='pessoa_create'),
    path('pessoa/<int:pk>/editar/', views.pessoa_edit, name='pessoa_edit'),
    path('pessoa/<int:pk>/deletar/', views.pessoa_delete, name='pessoa_delete'),


    path('emprestimos/', views.emprestimos_list, name='emprestimos_list'),
    
]
