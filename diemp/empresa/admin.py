from django.contrib import admin
from diemp.empresa.models import Inscricao


class InscricaoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'email', 'phone')
    search_fields = ('name', 'cnpj', 'phone')
    list_filter = ('created_at',)

admin.site.register(Inscricao, InscricaoModelAdmin)
