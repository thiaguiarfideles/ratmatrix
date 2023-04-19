from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from rat_s.models import DadosPessoais, Medico
from rat_s.resources import MedicoResource



# Register your models here.
admin.site.register(DadosPessoais)

@admin.register(Medico)
class MedicoAdmin(ImportExportModelAdmin):
    resource_class = MedicoResource


