from django.shortcuts import render, redirect, HttpResponse
from .forms import FormCategoria
from django.contrib import messages
from .models import Categoria, Esquadrao

def home (request):
    form_categoria = FormCategoria()
    categorias = Categoria.objects.all()
    context = {
        'form_categoria' : form_categoria,
        'categorias' : categorias
    }
    return render (request, 'home.html', context)

def cadastrar_categoria(request):
    if request.method == 'POST':
        form_categoria = FormCategoria(request.POST)
        
        if form_categoria.is_valid():
            messages.success(request, 'Categoria cadastrada com sucesso')
            form_categoria.save();
            return redirect ('/')
        else:
            messages.error(request, 'Não foi possível cadastrar a categoria')
            return redirect ('/')

def ver_equipamento(request, id):
    return render (request, 'ver_equipamento.html')

def ver_esquadroes(request):
    esquadroes = Esquadrao.objects.all();
    
    context = {
        'esquadroes' : esquadroes,
    }
    return render (request, 'ver_esquadroes.html', context)