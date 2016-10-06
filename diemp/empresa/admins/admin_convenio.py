from django.contrib import admin


class ConveniosModelAdmin(admin.ModelAdmin):
    list_display = ('Empresa', 'numero')
    search_fields = ('Empresa', 'numero')

    def related_empresa(self, obj):
        return obj.id_empresa.nome
        related_empresa.short_description = 'Empresa'