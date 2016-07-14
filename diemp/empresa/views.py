from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from diemp.empresa.forms import EmpresaForm
from diemp.empresa.models import Inscricao

def inscricao(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = EmpresaForm(request.POST)

    if not form.is_valid():
        return render(request, 'empresa/cad_empresa.html', {'form': form})

    Inscricao.objects.create(**form.cleaned_data)
    messages.success(request, 'Inscrição realizada com sucesso!')

    return HttpResponseRedirect('/empresa/')


def new(request):
    return render(request, 'empresa/cad_empresa.html', {'form': EmpresaForm()})