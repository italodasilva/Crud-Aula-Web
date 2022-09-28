"""ListaWeb2Tri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ListaWeb2Tri.Views import paginas, Departamento, Funcionario, Habilitacao, Pessoa, Corretor, TelefoneCorretor, CorGerCor, Municipio, Regiao, CorAtendeReg

urlpatterns = [
    path('', paginas.index),
    path('index', paginas.index, name='index'),

    path('home1', paginas.home1, name='home1'),
    path('home2', paginas.home2, name='home2'),
    path('home3', paginas.home3, name='home3'),

    path('departamento', Departamento.listar, name='departamento'),
    path('departamento/criar', Departamento.criar, name='departamento.criar'),
    path('departamento/editar/<id>', Departamento.editar, name='departamento.editar'),
    path('departamento/excluir/<id>', Departamento.excluir, name='departamento.excluir'),

    path('funcionario', Funcionario.listar, name='funcionario'),
    path('funcionario/criar', Funcionario.criar, name='funcionario.criar'),
    path('funcionario/editar/<id>', Funcionario.editar, name='funcionario.editar'),
    path('funcionario/excluir/<id>', Funcionario.excluir, name='funcionario.excluir'),

    path('habilitacao', Habilitacao.listar, name='habilitacao'),
    path('habilitacao/criar', Habilitacao.criar, name='habilitacao.criar'),
    path('habilitacao/editar/<id>', Habilitacao.editar, name='habilitacao.editar'),
    path('habilitacao/excluir/<id>', Habilitacao.excluir, name='habilitacao.excluir'),

    path('pessoa', Pessoa.listar, name='pessoa'),
    path('pessoa/criar', Pessoa.criar, name='pessoa.criar'),
    path('pessoa/editar/<id>', Pessoa.editar, name='pessoa.editar'),
    path('pessoa/excluir/<id>', Pessoa.excluir, name='pessoa.excluir'),

    path('corretor', Corretor.listar, name='corretor'),
    path('corretor/criar', Corretor.criar, name='corretor.criar'),
    path('corretor/editar/<id>', Corretor.editar, name='corretor.editar'),
    path('corretor/excluir/<id>', Corretor.excluir, name='corretor.excluir'),

    path('telefonecorretor', TelefoneCorretor.listar, name='telefonecorretor'),
    path('telefonecorretor/criar', TelefoneCorretor.criar, name='telefonecorretor.criar'),
    path('telefonecorretor/editar/<id>', TelefoneCorretor.editar, name='telefonecorretor.editar'),
    path('telefonecorretor/excluir/<id>', TelefoneCorretor.excluir, name='telefonecorretor.excluir'),

    path('corgercor', CorGerCor.listar, name='corgercor'),
    path('corgercor/criar', CorGerCor.criar, name='corgercor.criar'),
    path('corgercor/editar/<id>', CorGerCor.editar, name='corgercor.editar'),
    path('corgercor/excluir/<id>', CorGerCor.excluir, name='corgercor.excluir'),

    path('municipio', Municipio.listar, name='municipio'),
    path('municipio/criar', Municipio.criar, name='municipio.criar'),
    path('municipio/editar/<id>', Municipio.editar, name='municipio.editar'),
    path('municipio/excluir/<id>', Municipio.excluir, name='municipio.excluir'),

    path('regiao', Regiao.listar, name='regiao'),
    path('regiao/criar', Regiao.criar, name='regiao.criar'),
    path('regiao/editar/<id>', Regiao.editar, name='regiao.editar'),
    path('regiao/excluir/<id>', Regiao.excluir, name='regiao.excluir'),

    path('coratendereg', CorAtendeReg.listar, name='coratendereg'),
    path('coratendereg/criar', CorAtendeReg.criar, name='coratendereg.criar'),
    path('coratendereg/editar/<id>', CorAtendeReg.editar, name='coratendereg.editar'),
    path('coratendereg/excluir/<id>', CorAtendeReg.excluir, name='coratendereg.excluir'),

]
