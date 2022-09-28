from django.shortcuts import get_object_or_404, redirect, render
from ListaWeb2Tri.models import *
from django.forms import ModelForm

class MunicipioForm(ModelForm):
    class Meta:
        model = Municipio
        fields = '__all__'

def listar(request):
    municipio =  Municipio.objects.all()

    return render(request, 'Municipio/lista.html', {
        'municipio': municipio
    })


def criar(request):
    frm = MunicipioForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('municipio')

    return render(request, 'Municipio/form.html',{
        'titulo' : 'Cadastrar município',
        'frm':frm
    })

def editar(request,id):
    municipio = get_object_or_404(Municipio, pk=id)
    frm = MunicipioForm(request.POST or None, instance=municipio)

    if frm.is_valid():
        frm.save()
        return redirect('municipio')

    return render(request, 'Municipio/form.html',{
        'titulo' : 'Editar município',
        'frm':frm
    })

def excluir(request,id):
    municipio = get_object_or_404(Municipio, pk=id)
    municipio.delete()

    return redirect('municipio')