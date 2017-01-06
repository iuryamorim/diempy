from io import TextIOWrapper
import csv

from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r

from diemp.aluno.forms import ImportForm
from diemp.aluno.models.model_aluno import Inscricao
from diemp.aluno.models.model_curso import Curso
from diemp.aluno.models.model_pessoacurso import PessoaCurso


def new(request):
    if not request.user.is_authenticated():
        return call_login(request)
    else:
        return create(request)


def call_login(request):
    return HttpResponseRedirect(r('login:login'))


def create(request):
    if request.method == "POST":
        form = ImportForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'aluno/import_csv.html', {'form': form})

        
        try:
            handle_files(request)
        except:
            return render(request, 'aluno/import_csv.html', {'form': form, 'error': True})
        return render(request, 'aluno/import_csv.html', {'form': form, 'success': True})
    return render(request, 'aluno/import_csv.html', {'form': ImportForm()})


def handle_files(request):
    f = TextIOWrapper(request.FILES['file'].file, encoding=request.encoding)
    reader = csv.DictReader(f)
    for row in reader:
                
        for r in row.keys():
            if row[r] == 'NULL':
                row[r] = None                    

        obj = Inscricao(nome=row['NOME_ALUNO'], email=row['E_MAIL'], cpf=row['CPF'], dt_nasc=row['DT_NASCIMENTO'], situacao=row['SITUACAO'],
                        ddi_residencial=row['DDI_RESIDENCIAL'], ddd_residencial=row['DDD_RESIDENCIAL'],
                        fone_residencial=row['FONE_RESIDENCIAL'],
                        ddi_comercial=row['DDI_COMERCIAL'], ddd_comercial=row['DDD_COMERCIAL'], fone_comercial=row['FONE_COMERCIAL'],
                        ddi_celular=row['DDI_CELULAR'], ddd_celular=row['DDD_CELULAR'], fone_celular=row['FONE_CELULAR'],
                        tipo_logradouro=row['TIPO_LOGRADOURO'],
                        logradouro=row['LOGRADOURO'], numero=row['NUMERO'], complemento=row['COMPLEMENTO'], bairro=row['BAIRRO'], cep=row['CEP'],
                        distrito=row['DISTRITO'],
                        municipio=row['MUNICIPIO'], uf=row['UF'], pais=row['PAIS'])

        try:
            objAluno = Inscricao.objects.get(cpf=row['CPF'])
            id = objAluno.pk
        except:
            id = None

        if id:
            obj.id = id
        obj.save()
        
        try:
            obj_curso = Curso.objects.get(cod_curso=row['COD_CURSO'])
        except:
            obj_curso = Curso.objects.create(cod_curso=row['COD_CURSO'], unidade=row['UNIDADE'], nome=row['CURSO'])
        try:
            objpessoacurso = PessoaCurso.objects.get(id_pessoa=obj.pk)
        except:
            objpessoacurso = None
        if objpessoacurso:
            if (objpessoacurso.id_curso == obj_curso.pk):
                continue
        
        obj_ps = PessoaCurso(nome_curso=obj_curso, nome_aluno=obj, matricula=row['MATRICULA'])
        obj_ps.save()
    return True
