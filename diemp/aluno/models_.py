from django.db import models

class Inscricao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)   
    nome = models.CharField(db_column='Nome', max_length=100)   
    email = models.CharField(db_column='Email', max_length=150, blank=True, null=True)   
    cpf = models.CharField(db_column='Cpf', unique=True, max_length=20)   
    dt_nasc = models.DateField(db_column='Dt_Nasc', blank=True, null=True)   
    situacao = models.CharField(db_column='Situacao', max_length=25, blank=True, null=True)   
    ddi_residencial = models.IntegerField(db_column='Ddi_Residencial', blank=True, null=True)   
    ddd_residencial = models.IntegerField(db_column='Ddd_Residencial', blank=True, null=True)   
    fone_residencial = models.CharField(db_column='Fone_Residencial', max_length=15, blank=True, null=True)   
    ddi_comercial = models.IntegerField(db_column='Ddi_Comercial', blank=True, null=True)   
    ddd_comercial = models.IntegerField(db_column='Ddd_Comercial', blank=True, null=True)   
    fone_comercial = models.CharField(db_column='Fone_Comercial', max_length=15, blank=True, null=True)   
    ddi_celular = models.IntegerField(db_column='Ddi_Celular', blank=True, null=True)   
    ddd_celular = models.IntegerField(db_column='Ddd_Celular', blank=True, null=True)   
    fone_celular = models.CharField(db_column='Fone_Celular', max_length=15, blank=True, null=True)   
    tipo_logradouro = models.CharField(db_column='Tipo_logradouro', max_length=10, blank=True, null=True)   
    logradouro = models.CharField(db_column='Logradouro', max_length=255, blank=True, null=True)   
    numero = models.CharField(db_column='Numero', max_length=10, blank=True, null=True)   
    complemento = models.CharField(db_column='Complemento', max_length=150, blank=True, null=True)   
    bairro = models.CharField(db_column='Bairro', max_length=150, blank=True, null=True)   
    cep = models.CharField(db_column='Cep', max_length=15, blank=True, null=True)   
    distrito = models.CharField(db_column='Distrito', max_length=150, blank=True, null=True)   
    municipio = models.CharField(db_column='Municipio', max_length=150, blank=True, null=True)   
    uf = models.CharField(db_column='Uf', max_length=2, blank=True, null=True)   
    pais = models.CharField(db_column='Pais', max_length=100, blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'Pessoa'

        verbose_name_plural = 'alunos'
        verbose_name = 'aluno'
        ordering = ('-id',)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nome = models.CharField(db_column='Nome', max_length=255)
    unidade = models.CharField(db_column='Unidade', max_length=100)
    cod_curso = models.CharField(db_column='Cod_Curso', max_length=50)

    class Meta:
        managed = False
        db_table = 'Curso'
        verbose_name_plural = 'cursos'
        verbose_name = 'curso'
        ordering = ('-id',)

    def __str__(self):
        return self.nome


class PessoaCurso(models.Model):
    matricula = models.CharField(db_column='Matricula', max_length=100)   
    id_curso = models.ForeignKey(Curso, db_column='ID_CURSO', name='Curso')   
    id_pessoa = models.ForeignKey(Inscricao, db_column='Id_Pessoa', blank=True, null=True, name='Aluno')   

    class Meta:
        managed = False
        db_table = 'Pessoa__Curso'

