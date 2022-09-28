from django.shortcuts import get_object_or_404, redirect, render
from ListaWeb2Tri.models import *
from django.forms import ModelForm

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

def listar(request):
    pessoa =  Pessoa.objects.all()

    return render(request, 'Pessoa/lista.html', {
        'pessoa': pessoa
    })


def criar(request):
    frm = PessoaForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('pessoa')

    return render(request, 'Pessoa/form.html',{
        'titulo' : 'Cadastrar pessoa',
        'frm':frm
    })

def editar(request,id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    frm = PessoaForm(request.POST or None, instance=pessoa)

    if frm.is_valid():
        frm.save()
        return redirect('pessoa')

    return render(request, 'Pessoa/form.html',{
        'titulo' : 'Editar pessoa',
        'frm':frm
    })

def excluir(request,id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    pessoa.delete()

    return redirect('pessoa')