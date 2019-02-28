from django.shortcuts import render
from biblioteca.form import LivroForm
from biblioteca.models import Livro

# Create your views here.
def render_index(request):
    # listar livros cadastrados por data de publicação
    #
    return render(request, 'index.html', {})

def render_cadastrar_livros(request):

    if request.method == 'POST':
        livro_form = LivroForm(request.POST)
        print(livro_form)
        if livro_form.is_valid():
            livro = Livro()
            livro.titulo = livro_form.cleaned_data['titulo']
            livro.lancamento = livro_form.cleaned_data['lancamento']
            livro.descricao = livro_form.cleaned_data['descricao']
            livro.autor = livro_form.cleaned_data['autor']
            livro.genero = livro_form.cleaned_data['genero']
            livro.save()
            return render(request, 'sucesso.html')

    return render(request, 'cadastro_livros.html', {'form': LivroForm})
