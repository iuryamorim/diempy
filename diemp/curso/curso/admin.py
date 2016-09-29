from django.contrib import admin
from import_export import resources
from diemp.aluno.models import Inscricao
from import_export.admin import ImportExportModelAdmin


class InscricaoModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')
    search_fields = ('nome', 'cpf')


class AlunoResource(resources.ModelResource):
    class Meta:
        model = Inscricao

class AlunoAdmin(ImportExportModelAdmin):
    resource_class = AlunoResource

admin.site.register(Inscricao, InscricaoModelAdmin)

