from django.contrib import admin

class PessoaCursoModelAdmin(admin.ModelAdmin):
    list_display = ('Aluno', 'Matrícula', 'Curso')
    search_fields = ('Aluno', 'Matrícula', 'Curso')