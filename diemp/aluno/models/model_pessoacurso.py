from django.db import models
from diemp.aluno.models.model_aluno import Inscricao
from diemp.aluno.models.model_curso import Curso


class PessoaCurso(models.Model):
    matricula = models.CharField(db_column='Matricula', max_length=100)
    nome_curso = models.ForeignKey(Curso, db_column='ID_CURSO')
    nome_aluno = models.ForeignKey(Inscricao, db_column='Id_Pessoa')
