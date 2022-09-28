from django.shortcuts import get_object_or_404, redirect, render
from ListaWeb2Tri.models import *
from django.forms import ModelForm

class RegiaoForm(ModelForm):
    class Meta:
        model = Regiao
        fields = '__all__'

def listar(request):
    regiao =  Regiao.objects.all()

    return render(request, 'Regiao/lista.html', {
        'regiao': regiao
    })


def criar(request):
    frm = RegiaoForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('regiao')

    return render(request, 'Regiao/form.html',{
        'titulo' : 'Cadastrar região',
        'frm':frm
    })

def editar(request,id):
    regiao = get_object_or_404(Regiao, pk=id)
    frm = RegiaoForm(request.POST or None, instance=regiao)

    if frm.is_valid():
        frm.save()
        return redirect('regiao')

    return render(request, 'Regiao/form.html',{
        'titulo' : 'Editar região',
        'frm':frm
    })

def excluir(request,id):
    regiao = get_object_or_404(Regiao, pk=id)
    regiao.delete()

    return redirect('regiao')