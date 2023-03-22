from django import forms

from .models import LivroVisitas


class LivroVisitasModelForm(forms.ModelForm):
    class Meta:
        model = LivroVisitas
        fields = ['nome', 'cidade', 'comentario']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'comentario': forms.TextInput(attrs={'class': 'form-control'}),

        }
