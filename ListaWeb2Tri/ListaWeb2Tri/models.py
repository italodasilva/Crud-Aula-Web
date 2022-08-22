from tkinter.messagebox import YES
from django.db import models

#Questão1
class Departamento (models.Model):
    codigo = models.CharField(max_length=50, primary_key=True)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.codigo

class Funcionario(models.Model):
    matricula = models.CharField(max_length=30, primary_key=True)
    nome = models.CharField(max_length=200)
    codigodep = models.ForeignKey(Departamento, on_delete=models.CASCADE)

#Questão2
class Habilitacao(models.Model):
    numeroHab = models.CharField(max_length=30, primary_key=True)
    validadeHab = models.DateField()

    def __str__(self):
        return self.numeroHab

class Pessoa(models.Model):
    codigo = models.CharField(max_length=30, primary_key=True)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    CartHab = models.ForeignKey(Habilitacao, on_delete=models.CASCADE)

#Questão3
class Corretor(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    comissao = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.cpf

class TelefoneCorretor(models.Model):
    cpfCorretor = models.ForeignKey(Corretor, on_delete=models.CASCADE)
    area = models.CharField(max_length=10)
    numero = models.CharField(max_length=20)

class CorGerCor(models.Model):
    cpfGerenciador = models.ForeignKey(Corretor, on_delete=models.CASCADE, related_name='Gerenciador')
    cpfGerenciado = models.ForeignKey(Corretor, on_delete=models.CASCADE, related_name='Gerenciado')

class Municipio(models.Model):
    nome = models.CharField(max_length=200)
    uf = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Regiao(models.Model):
    nome = models.CharField(max_length=200)
    IdMunicipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class CorAtendeReg(models.Model):
    cpfCorretor = models.ForeignKey(Corretor, on_delete=models.CASCADE)
    IdRegiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)