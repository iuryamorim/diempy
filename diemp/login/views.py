from io import TextIOWrapper
import csv

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r

from diemp.aluno.forms import LoginForm, ImportForm
from diemp.aluno.models.model_aluno import Inscricao
from diemp.aluno.models.model_curso import Curso
from diemp.aluno.models.model_pessoacurso import PessoaCurso


def new(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            return create(request)
        return empty_form(request)
    else:
        return call_import(request)


def create(request):
    form = LoginForm(request.POST)

    if not form.is_valid():
        return render(request, 'aluno/login.html', {'form': form})

    user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

    if user is not None:
        login(request, user)
        return call_import(request)
    else:
        return render(request, 'aluno/login.html', {'form': form})


def empty_form(request):
    return render(request, 'aluno/login.html', {'form': LoginForm()})


def call_import(request):
    return HttpResponseRedirect(r('aluno:import', 'import'))



def import_csv(request, arg):
    if request.method == "POST":
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            handle_files(request)
    return render(request, 'aluno/import_csv.html', {'form': ImportForm()})


def handle_files(request):
    f = TextIOWrapper(request.FILES['file'].file, encoding=request.encoding)
    reader = csv.reader(f)
    cont = 0
    for row in reader:
        if cont != 0 :
            NOME = row[0]
            CPF = row[4]
            SITUACAO = row[6]
            DDI_RESIDENCIAL = row[7]
            DDD_RESIDENCIAL = row[8]
            FONE_RESIDENCIAL = row[9]
            DDI_COMERCIAL = row[10]
            DDD_COMERCIAL = row[11]
            FONE_COMERCIAL = row[12]
            DDI_CELULAR = row[13]
            DDD_CELULAR = row[14]
            FONE_CELULAR = row[15]
            TIPO_LOGRADOURO = row[16]
            LOGRADOURO = row[17]
            NUMERO = row[18]
            COMPLEMENTO = row[19]
            BAIRRO = row[20]
            CEP = row[21]
            DISTRITO = row[22]
            MUNICIPIO = row[23]
            UF = row[24]
            PAIS = row[25]
            EMAIL = row[26]
            DT_NASC = row[27].split('/')
            DT_NASC = (DT_NASC[2] + '-' + DT_NASC[1] + '-' + DT_NASC[0])

            aux = None
            try:
                aux = Inscricao.objects.get(cpf=CPF)
            except:
                aux = None

            if not aux:
                obj = Inscricao(nome=NOME, email=EMAIL, cpf=CPF, dt_nasc=DT_NASC, situacao=SITUACAO,
                                ddi_residencial=DDI_RESIDENCIAL, ddd_residencial=DDD_RESIDENCIAL,
                                fone_residencial=FONE_RESIDENCIAL,
                                ddi_comercial=DDI_COMERCIAL, ddd_comercial=DDD_COMERCIAL, fone_comercial=FONE_COMERCIAL,
                                ddi_celular=DDI_CELULAR, ddd_celular=DDD_CELULAR, fone_celular=FONE_CELULAR,
                                tipo_logradouro=TIPO_LOGRADOURO,
                                logradouro=LOGRADOURO, numero=NUMERO, complemento=COMPLEMENTO, bairro=BAIRRO, cep=CEP,
                                distrito=DISTRITO,
                                municipio=MUNICIPIO, uf=UF, pais=PAIS)
                obj.save()

                print(obj.pk)
                curso = Curso.objects.get(cod_curso=row[2])
                print(curso.pk)
                print(curso)
                break

            else:
                Inscricao.objects.update(nome=NOME, email=EMAIL, dt_nasc=DT_NASC, situacao=SITUACAO,
                            ddi_residencial=DDI_RESIDENCIAL, ddd_residencial=DDD_RESIDENCIAL,
                            fone_residencial=FONE_RESIDENCIAL,
                            ddi_comercial=DDI_COMERCIAL, ddd_comercial=DDD_COMERCIAL, fone_comercial=FONE_COMERCIAL,
                            ddi_celular=DDI_CELULAR, ddd_celular=DDD_CELULAR, fone_celular=FONE_CELULAR,
                            tipo_logradouro=TIPO_LOGRADOURO,
                            logradouro=LOGRADOURO, numero=NUMERO, complemento=COMPLEMENTO, bairro=BAIRRO, cep=CEP,
                            distrito=DISTRITO,
                            municipio=MUNICIPIO, uf=UF, pais=PAIS)
                print(1)
        else:
            cont += 1



def call_logout(request):
    logout(request)
    return HttpResponseRedirect(r('aluno:login'))