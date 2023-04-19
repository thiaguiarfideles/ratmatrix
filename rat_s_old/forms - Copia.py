

from django import forms
from rat_s.models import DadosPessoais


class DadosPessoaisForm(forms.ModelForm):
    class Meta:
        model = DadosPessoais
        fields = '__all__'

