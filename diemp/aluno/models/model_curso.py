from django.db import models


class Curso(models.Model):
    nome = models.CharField(db_column='Nome', max_length=255)
    unidade = models.CharField(db_column='Unidade', max_length=100)
    cod_curso = models.CharField(db_column='Cod_Curso', max_length=50)

    class Meta:
        verbose_name_plural = 'cursos'
        verbose_name = 'curso'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
