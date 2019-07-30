from django.shortcuts import render
from biblioteca.form import LivroForm
from biblioteca.models import Livro


# Create your views here.
def render_index(request):
    # Listar livros para utilizar no index
    # BÔNUS: Listar eles por ordem de data de publicação
    #
    return render(request, 'index.html', {})

def render_editoras_cadastradas_admin():
        return render(request, 'paginanaoexistente.html', {})


def render_cadastrar_livros():
    if request.method == 'POST':
        livro_form = LivroForm(request.POST)
        if livro_form.is_valid():
            livro = Livro()
            livro.titulo = livro_form.cleaned_data['titulo']
            livro.lancamento = livro_form.cleaned_data['lancamento']
            livro.autor = livro_form.cleaned_data.get['autor']
            livro.genero = livro_form.cleaned_data['genero']
            return render(request, 'sucesso.html')

    return render(request, 'cadastro_livros.html', {'form': LivroForm})
