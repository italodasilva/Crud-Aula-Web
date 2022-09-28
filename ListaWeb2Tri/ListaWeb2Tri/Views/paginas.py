from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def home1(request):
    return render(request, 'home1.html', {})

def home2(request):
    return render(request, 'home2.html', {})

def home3(request):
    return render(request, 'home3.html', {})