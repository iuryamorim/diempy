from django.db import models


class Curso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    unidade = models.CharField(db_column='Unidade', max_length=100)  # Field name made lowercase.
    cod_curso = models.CharField(db_column='Cod_Curso', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Curso'
        verbose_name_plural = 'cursos'
        verbose_name = 'curso'
        ordering = ('-id',)