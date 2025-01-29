from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    data_publicacao = models.DateField(null=True, blank=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
class Emprestimo(models.Model):
    Livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos')
    nome_usuário  = models.CharField(max_length=100)
    data_empresto = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, black=True)

    def __str__(self):
        return f"{self.nome_usuário} - {self.livro.titulo}"