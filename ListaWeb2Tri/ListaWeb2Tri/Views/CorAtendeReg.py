from django.shortcuts import get_object_or_404, redirect, render
from ListaWeb2Tri.models import *
from django.forms import ModelForm

class CorAtendeRegForm(ModelForm):
    class Meta:
        model = CorAtendeReg
        fields = '__all__'

def listar(request):
    coratendereg =  CorAtendeReg.objects.all()

    return render(request, 'CorAtendeReg/lista.html', {
        'coratendereg': coratendereg
    })


def criar(request):
    frm = CorAtendeRegForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('coratendereg')

    return render(request, 'CorAtendeReg/form.html',{
        'titulo' : 'Cadastrar Corretor atende Região',
        'frm':frm
    })

def editar(request,id):
    coratendereg = get_object_or_404(CorAtendeReg, pk=id)
    frm = CorAtendeRegForm(request.POST or None, instance=coratendereg)

    if frm.is_valid():
        frm.save()
        return redirect('coratendereg')

    return render(request, 'CorAtendeReg/form.html',{
        'titulo' : 'Editar Corretor atende Região',
        'frm':frm
    })

def excluir(request,id):
    coratendereg = get_object_or_404(CorAtendeReg, pk=id)
    coratendereg.delete()

    return redirect('coratendereg')