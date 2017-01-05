from django.contrib import admin

class PessoaCursoModelAdmin(admin.ModelAdmin):
    list_display = ('nome_aluno', 'matricula', 'nome_curso')
    search_fields = ('nome_aluno__nome', 'matricula', 'nome_curso__nome')

