from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('livros/', views.livros_list, name='livros_list'),
    path('livros/novo', views.livro_create, name='livro_create'),
    path('livros/<int:pk>/', views.livro_detail, name='livro_detail'),
    path('livros/<int:pk>/editar/', views.livro_update, name='livro_update'),
    path('livros/<int:pk>/delete/', views.livro_delete, name='livro_delete'),


    path('emprestimos/', views.emprestimos_list, name='emprestimos_list'),
    
]
