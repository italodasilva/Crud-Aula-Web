from django.shortcuts import get_object_or_404, redirect, render
from ListaWeb2Tri.models import *
from django.forms import ModelForm

class DepartamentoForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

def listar(request):
    funcionario =  Funcionario.objects.all()

    return render(request, 'Funcionario/lista.html', {
        'funcionario': funcionario
    })


def criar(request):
    frm = DepartamentoForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('funcionario')

    return render(request, 'Funcionario/form.html',{
        'titulo' : 'Cadastrar funcionário',
        'frm':frm
    })

def editar(request,id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    frm = DepartamentoForm(request.POST or None, instance=funcionario)

    if frm.is_valid():
        frm.save()
        return redirect('funcionario')

    return render(request, 'Funcionario/form.html',{
        'titulo' : 'Editar funcionário',
        'frm':frm
    })

def excluir(request,id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    funcionario.delete()

    return redirect('funcionario')