from django.db import models

class Inscricao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='Cpf', unique=True, max_length=20)  # Field name made lowercase.
    dt_nasc = models.DateField(db_column='Dt_Nasc', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='Situacao', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ddi_residencial = models.IntegerField(db_column='Ddi_Residencial', blank=True, null=True)  # Field name made lowercase.
    ddd_residencial = models.IntegerField(db_column='Ddd_Residencial', blank=True, null=True)  # Field name made lowercase.
    fone_residencial = models.CharField(db_column='Fone_Residencial', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ddi_comercial = models.IntegerField(db_column='Ddi_Comercial', blank=True, null=True)  # Field name made lowercase.
    ddd_comercial = models.IntegerField(db_column='Ddd_Comercial', blank=True, null=True)  # Field name made lowercase.
    fone_comercial = models.CharField(db_column='Fone_Comercial', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ddi_celular = models.IntegerField(db_column='Ddi_Celular', blank=True, null=True)  # Field name made lowercase.
    ddd_celular = models.IntegerField(db_column='Ddd_Celular', blank=True, null=True)  # Field name made lowercase.
    fone_celular = models.CharField(db_column='Fone_Celular', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tipo_logradouro = models.CharField(db_column='Tipo_logradouro', max_length=10, blank=True, null=True)  # Field name made lowercase.
    logradouro = models.CharField(db_column='Logradouro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=10, blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=150, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='Cep', max_length=15, blank=True, null=True)  # Field name made lowercase.
    distrito = models.CharField(db_column='Distrito', max_length=150, blank=True, null=True)  # Field name made lowercase.
    municipio = models.CharField(db_column='Municipio', max_length=150, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='Uf', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pessoa'

        verbose_name_plural = 'alunos'
        verbose_name = 'aluno'
        ordering = ('-id',)

    def __str__(self):
        return self.nome