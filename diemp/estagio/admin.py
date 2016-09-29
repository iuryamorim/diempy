from django.contrib import admin
from diemp.curso.models import Curso


class CursosModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade')
    search_fields = ('nome', 'unidade')


admin.site.register(Curso, CursosModelAdmin)

