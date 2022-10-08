from django.shortcuts import get_object_or_404, redirect, render
from ListaWeb2Tri.models import *
from django.forms import ModelForm

class CorGerCorForm(ModelForm):
    class Meta:
        model = CorGerCor
        fields = '__all__'

def listar(request):
    corgercor =  CorGerCor.objects.all()

    return render(request, 'CorGerCor/lista.html', {
        'corgercor': corgercor
    })


def criar(request):
    frm = CorGerCorForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('corgercor')

    return render(request, 'CorGerCor/form.html',{
        'titulo' : 'Cadastrar Gerenciador',
        'frm':frm
    })

def editar(request,id):
    corgercor = get_object_or_404(CorGerCor, pk=id)
    frm = CorGerCorForm(request.POST or None, instance=corgercor)

    if frm.is_valid():
        frm.save()
        return redirect('corgercor')

    return render(request, 'CorGerCor/form.html',{
        'titulo' : 'Editar Gerenciador',
        'frm':frm
    })

def excluir(request,id):
    corgercor = get_object_or_404(CorGerCor, pk=id)
    corgercor.delete()

    return redirect('corgercor')