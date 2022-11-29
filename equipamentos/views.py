from django.shortcuts import render, redirect, HttpResponse
from .forms import FormCategoria
from django.contrib import messages
from .models import Categoria, Esquadrao, Equipamento

def home (request, id):
    esquadrao = Esquadrao.objects.get(id = id)
    form_categoria = FormCategoria()
    categorias = Categoria.objects.all()
    
    equipamentos = Equipamento.objects.filter(esquadrao = esquadrao)
    set_categorias = set(categorias)
    
    context = {
        'form_categoria' : form_categoria,
        'categorias' : set_categorias,
        'esquadrao' : esquadrao,
        'equipamentos' : equipamentos
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
    equipamento = Equipamento.objects.get(id = id)
    context = {
        'equipamento' : equipamento
    }
    return render (request, 'ver_equipamento.html', context)

def ver_esquadroes(request):
    esquadroes = Esquadrao.objects.all();
    
    context = {
        'esquadroes' : esquadroes,
    }
    return render (request, 'ver_esquadroes.html', context)