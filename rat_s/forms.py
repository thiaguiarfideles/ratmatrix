from django import forms
from .models import DadosPessoais

class DadosPessoaisForm(forms.ModelForm):
    class Meta:
        model = DadosPessoais
        fields = ['nm_analista', 'nm_medico', 'nm_hospital', 'tel_contato', 'email', 'dt_atendimento', 'servico_analisado', 'upload', 'utiliza_protocolo', 'utiliza_rotina_especial', 'utiliza_rotina', 'comentarios']
        widgets = {
            'upload': forms.ClearableFileInput(attrs={'multiple': True}),
        }
