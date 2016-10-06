from django.contrib import admin
from diemp.estagio.models import Estagio


class EstagiosModelAdmin(admin.ModelAdmin):
    list_display = ('Aluno', 'Convenio')
    search_fields = ('Aluno', 'Convenio')

    def related_estagio(self, obj):
        return obj.id_aluno.nome
        related_estagio.short_description = 'Estagio'

    def related_convenio(self, obj):
        return obj.id_convenio.numero
        related_convenio.short_description = 'Convenio'

admin.site.register(Estagio, EstagiosModelAdmin)

