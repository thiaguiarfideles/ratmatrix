from import_export import resources
from .models import Medico

class MedicoResource(resources.ModelResource):
    class Meta:
        model = Medico
        fields = ('id','nm_medico', 'crm')