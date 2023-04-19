from django import forms
from django_select2.forms import ModelSelect2Mixin, Select2MultipleWidget
from .models import DadosPessoais

class DadosPessoaisForm(forms.ModelForm,ModelSelect2Mixin):
    class Meta:
        model = DadosPessoais
        fields = ['nm_analista', 'nm_medico', 'nm_hospital', 'tel_contato', 'email', 'dt_atendimento', 'servico_analisado', 'upload', 'utiliza_protocolo', 'utiliza_rotina_especial', 'utiliza_rotina', 'comentarios']
        widgets = {
            'upload': forms.ClearableFileInput(attrs={'multiple': True}),
            'nm_medico': Select2MultipleWidget,
        }
        search_fields = [
        'nm_medico__icontains',
        ]
        queryset = DadosPessoais.objects.all()
