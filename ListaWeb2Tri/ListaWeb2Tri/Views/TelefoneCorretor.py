from django.shortcuts import get_object_or_404, redirect, render
from ListaWeb2Tri.models import *
from django.forms import ModelForm

class TelefoneCorretorForm(ModelForm):
    class Meta:
        model = TelefoneCorretor
        fields = '__all__'

def listar(request):
    telefonecorretor =  TelefoneCorretor.objects.all()

    return render(request, 'TelefoneCorretor/lista.html', {
        'telefonecorretor': telefonecorretor
    })


def criar(request):
    frm = TelefoneCorretorForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('telefonecorretor')

    return render(request, 'TelefoneCorretor/form.html',{
        'titulo' : 'Cadastrar Telefone de um Corretor',
        'frm':frm
    })

def editar(request,id):
    telefonecorretor = get_object_or_404(TelefoneCorretor, pk=id)
    frm = TelefoneCorretorForm(request.POST or None, instance=telefonecorretor)

    if frm.is_valid():
        frm.save()
        return redirect('telefonecorretor')

    return render(request, 'TelefoneCorretor/form.html',{
        'titulo' : 'Editar Telefone de um Corretor',
        'frm':frm
    })

def excluir(request,id):
    telefonecorretor = get_object_or_404(TelefoneCorretor, pk=id)
    telefonecorretor.delete()

    return redirect('telefonecorretor')