class Livro():
    titulo = models.CharField(max_length=200)
    lancamento = models.DateField()
    descricao = models.TextField()
    autor = models.CharField(max_lenght=256, default='')
    genero = models.CharField(max_length=256, default='')

    def __str_():
        return self.titulo

class Editora():
    nome = models.CharField(max_length=200)
    pais = models.charField(max_lenght=200)
    livro = models.ForeignKey(Livro, on_dlete=models.SET_DEFAULT, default='')
