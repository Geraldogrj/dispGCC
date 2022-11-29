from django.shortcuts import render, redirect, HttpResponse
from .forms import FormCategoria, FormEquipamento
from django.contrib import messages
from .models import Categoria, Esquadrao, Equipamento

def home (request, id):
    esquadrao = Esquadrao.objects.get(id = id)
    form_categoria = FormCategoria()
    categorias = Categoria.objects.all()
    form_equipamento = FormEquipamento()
    
    equipamentos = Equipamento.objects.filter(esquadrao = esquadrao)
    set_categorias = set(categorias)
    
    context = {
        'form_categoria' : form_categoria,
        'categorias' : set_categorias,
        'esquadrao' : esquadrao,
        'equipamentos' : equipamentos,
        'form_equipamento' : form_equipamento,
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
    form_categoria = FormCategoria()
    form_equipamento = FormEquipamento()
    context = {
        'equipamento' : equipamento,
        'form_categoria': form_categoria,
        'form_equipamento' : form_equipamento,
    }
    return render (request, 'ver_equipamento.html', context)

def ver_esquadroes(request):
    esquadroes = Esquadrao.objects.all()
    form_categoria = FormCategoria()
    form_equipamento = FormEquipamento()
    
    context = {
        'esquadroes' : esquadroes,
        'form_categoria':form_categoria,
        'form_equipamento' : form_equipamento,
    }
    return render (request, 'ver_esquadroes.html', context)

def cadastrar_equipamento(request):
    if request.method == 'POST':
        form_equipamento = FormEquipamento(request.POST)
        
        if form_equipamento.is_valid():
            messages.success(request, 'Equipamento Cadastrado com sucesso')
            form_equipamento.save()
            return redirect ('/')
        else:
            messages.error(request, 'O equipamento não pode ser cadastrado')
            return redirect ('/')