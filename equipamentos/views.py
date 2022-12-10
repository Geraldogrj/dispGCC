from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import FormCategoria, FormEquipamento
from django.contrib import messages
from .models import Categoria, Esquadrao, Equipamento
from datetime import datetime

def tratar_virgula(campo):
    novo_campo = campo.replace(",", ".")
    return novo_campo
    

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
    categorias = Categoria.objects.all()
    data_atualizacao = datetime.today()
    context = {
        'equipamento' : equipamento,
        'form_categoria': form_categoria,
        'form_equipamento' : form_equipamento,
        'categorias': categorias,
        'data_atualizacao' : data_atualizacao,
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
        
def atualizar_equipamento(request, id):
    if request.method == "POST":
        
        equipamento = get_object_or_404(Equipamento, id = id)
        
        form = FormEquipamento(request.POST or None, instance= equipamento)
        
        print("*******************************")
        print(form.errors)
        print("*******************************")
        
        esquadrao = get_object_or_404(Esquadrao, pk = equipamento.esquadrao.pk)
        #categoria = Categoria.objects.get(nome = form.data['categoria'])
        categoria = get_object_or_404(Categoria, pk = int(form.data['categoria'])) 
        
    
        #Tratar as vírgulas
        peso = float(tratar_virgula(form.data['peso']))
        volume = float(tratar_virgula(form.data['volume']))
        largura = float(tratar_virgula(form.data['largura']))
        altura = float(tratar_virgula(form.data['altura']))
        comprimento = float(tratar_virgula(form.data['comprimento']))
        
        if form.is_valid():
            messages.success(request, 'O equipamento foi atualizado com sucesso')
            form.instance.esquadrao = esquadrao
            form.instance.peso = peso
            form.instance.volume = volume
            form.instance.esquadrao = esquadrao
            form.instance.largura = largura
            form.instance.altura = altura
            form.instance.comprimento = comprimento
            form.instance.categoria = categoria
            form.instance.data_atualizacao = datetime.today()
            form.save()
            return redirect ('/')
        else:
            messages.error(request, 'Não foi possível atualizar o equipamento')
            return redirect ('/')

