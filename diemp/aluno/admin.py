from django.contrib import admin
from diemp.aluno.models import Inscricao, PessoaCurso


class InscricaoModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')
    search_fields = ('nome', 'cpf')

admin.site.register(Inscricao, InscricaoModelAdmin)

class PessoaCursoModelAdmin(admin.ModelAdmin):
    list_display = ('Aluno', 'Curso')
    search_fields = ('Aluno', 'Curso')

admin.site.register(PessoaCurso, PessoaCursoModelAdmin)

