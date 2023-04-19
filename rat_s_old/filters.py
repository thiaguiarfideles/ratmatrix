import django_filters
from .models import DadosPessoais

class DadosPessoaisFilter(django_filters.FilterSet):
    nm_medico = django_filters.CharFilter(field_name='nm_medico__nome', lookup_expr='icontains')
    
    class Meta:
        model = DadosPessoais
        fields = ['nm_medico']