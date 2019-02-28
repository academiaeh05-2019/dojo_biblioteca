from biblioteca.choices import CHOICES_GENERO
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class LivroForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LivroForm, self).__init__(*args, **kwargs)

    titulo = forms.CharField(
        max_length=80,
        label='Titulo do livro',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'id' : 'titulo'
            }
        )
    )

    autor = forms.CharField(
        max_length=80,
        label='Autor',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'id' : 'autor'
            }
        )
    )

    lancamento = forms.DateField(
        label='Data de Lançamento',
        widget=DateInput(
            attrs={
                'required' : True,
            }
        )
    )

    genero = forms.CharField(
        max_length=20,
        label='Gênero',
        widget=forms.Select(
            choices=CHOICES_GENERO,
            attrs={
                'required' : True,
                'id' : 'genero'
            }
        )
    )


    descricao = forms.CharField(
        label='Descrição para livro',
        widget=forms.Textarea(
            attrs={
                "rows":7,
                "cols":99
            }
        )
    )
