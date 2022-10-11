from django.shortcuts import get_object_or_404, redirect, render
from ListaWeb2Tri.models import *
from django.forms import ModelForm

class HabilitacaoForm(ModelForm):
    class Meta:
        model = Habilitacao
        fields = '__all__'

def listar(request):
    habilitacao =  Habilitacao.objects.all()

    return render(request, 'Habilitacao/lista.html', {
        'habilitacao': habilitacao
    })


def criar(request):
    frm = HabilitacaoForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('habilitacao')

    return render(request, 'Habilitacao/form.html',{
        'titulo' : 'Cadastrar habilitação',
        'frm':frm
    })

def editar(request,id):
    habilitacao = get_object_or_404(Habilitacao, pk=id)
    frm = HabilitacaoForm(request.POST or None, instance=habilitacao)

    if frm.is_valid():
        frm.save()
        return redirect('habilitacao')

    return render(request, 'Habilitacao/form.html',{
        'titulo' : 'Editar habilitação',
        'frm':frm
    })

def excluir(request,id):
    habilitacao = get_object_or_404(Habilitacao, pk=id)
    habilitacao.delete()

    return redirect('habilitacao')