from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    lancamento = models.DateField()
    descricao = models.TextField()
    autor = models.CharField(max_length=256, default='')
    genero = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.titulo

class Editora(models.Model):
    nome = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    livro = models.ForeignKey(Livro, on_delete=models.SET_DEFAULT, default='')
