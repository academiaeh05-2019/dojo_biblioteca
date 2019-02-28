from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    lancamento = models.DateField()
    descricao = models.CharField(max_length=2000)

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=200)
    livro = models.ForeignKey(Livro, on_delete=models.SET_DEFAULT, default='')

class Editora(models.Model):
    nome = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    livro = models.ForeignKey(Livro, on_delete=models.SET_DEFAULT, default='')

class Genero(models.Model):
    nome = models.CharField(max_length=50)
    livro = models.ForeignKey(Livro, on_delete=models.SET_DEFAULT, default='')