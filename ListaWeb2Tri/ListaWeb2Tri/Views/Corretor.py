from django.shortcuts import get_object_or_404, redirect, render
from ListaWeb2Tri.models import *
from django.forms import ModelForm

class CorretorForm(ModelForm):
    class Meta:
        model = Corretor
        fields = '__all__'

def listar(request):
    corretor =  Corretor.objects.all()

    return render(request, 'Corretor/lista.html', {
        'corretor': corretor
    })


def criar(request):
    frm = CorretorForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('corretor')

    return render(request, 'Corretor/form.html',{
        'titulo' : 'Cadastrar corretor',
        'frm':frm
    })

def editar(request,id):
    corretor = get_object_or_404(Corretor, pk=id)
    frm = CorretorForm(request.POST or None, instance=corretor)

    if frm.is_valid():
        frm.save()
        return redirect('corretor')

    return render(request, 'Corretor/form.html',{
        'titulo' : 'Editar corretor',
        'frm':frm
    })

def excluir(request,id):
    corretor = get_object_or_404(Corretor, pk=id)
    corretor.delete()

    return redirect('corretor')