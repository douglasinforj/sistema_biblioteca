from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.livros_list, name='livros_list'),
]
