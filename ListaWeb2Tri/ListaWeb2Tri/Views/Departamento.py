from django.shortcuts import get_object_or_404, redirect, render
from ListaWeb2Tri.models import *
from django.forms import ModelForm

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

def listar(request):
    departamento =  Departamento.objects.all()

    return render(request, 'Departamento/lista.html', {
        'departamento': departamento
    })


def criar(request):
    frm = DepartamentoForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('departamento')

    return render(request, 'Departamento/form.html',{
        'titulo' : 'Cadastrar departamento',
        'frm':frm
    })

def editar(request,id):
    departamento = get_object_or_404(Departamento, pk=id)
    frm = DepartamentoForm(request.POST or None, instance=departamento)

    if frm.is_valid():
        frm.save()
        return redirect('departamento')

    return render(request, 'Departamento/form.html',{
        'titulo' : 'Editar departamento',
        'frm':frm
    })

def excluir(request,id):
    departamento = get_object_or_404(Departamento, pk=id)
    departamento.delete()

    return redirect('departamento')