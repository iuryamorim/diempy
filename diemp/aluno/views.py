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

        DTNASC = is_none(row['DT_NASCIMENTO'])
        if is_none(row['DT_NASCIMENTO']):
            try:
                DTNASC = DTNASC.split("/")
                DTNASC = DTNASC[2] + "-" + DTNASC[1] + "-" + DTNASC[0]
            except Exception as e:
                DTNASC = None
                print("Erro ao parsear a Data de Nascimento do cpf: " + is_none(row['CPF']))
                print(e)

        obj = Inscricao(nome=is_none(row['NOME_ALUNO']), email=is_none(row['E_MAIL']), cpf=is_none(row['CPF']), dt_nasc=DTNASC, situacao=is_none(row['SITUACAO']),
                        ddi_residencial=is_none(row['DDI_RESIDENCIAL']), ddd_residencial=is_none(row['DDD_RESIDENCIAL']),
                        fone_residencial=is_none(row['FONE_RESIDENCIAL']),
                        ddi_comercial=is_none(row['DDI_COMERCIAL']), ddd_comercial=is_none(row['DDD_COMERCIAL']), fone_comercial=is_none(row['FONE_COMERCIAL']),
                        ddi_celular=is_none(row['DDI_CELULAR']), ddd_celular=is_none(row['DDD_CELULAR']), fone_celular=is_none(row['FONE_CELULAR']),
                        tipo_logradouro=is_none(row['TIPO_LOGRADOURO']),
                        logradouro=is_none(row['LOGRADOURO']), numero=is_none(row['NUMERO']), complemento=is_none(row['COMPLEMENTO']), bairro=is_none(row['BAIRRO']), cep=is_none(row['CEP']),
                        distrito=is_none(row['DISTRITO']),
                        municipio=is_none(row['MUNICIPIO']), uf=is_none(row['UF']), pais=is_none(row['PAIS']))

        try:
            objAluno = Inscricao.objects.get(cpf=is_none(row['CPF']))
            id = objAluno.pk
        except:
            id = None

        if id:
            obj.id = id
        try:
            obj.save()
        except Exception as err:
            print(err)
            continue

        try:
            obj_curso = Curso.objects.get(cod_curso=is_none(row['COD_CURSO']))
        except:
            obj_curso = Curso.objects.create(cod_curso=is_none(row['COD_CURSO']),
                                unidade=is_none(row['UNIDADE']), nome=is_none(row['CURSO']))
        try:
            objpessoacurso = PessoaCurso.objects.get(id_pessoa=obj.pk)
        except:
            objpessoacurso = None
        if objpessoacurso:
            if (objpessoacurso.id_curso == obj_curso.pk):
                continue
        
        obj_ps = PessoaCurso(nome_curso=obj_curso, nome_aluno=obj, matricula=is_none(row['MATRICULA']))
        obj_ps.save()
    return True


def is_none(value):
    if len(value) == 0:
        return None
    return value
