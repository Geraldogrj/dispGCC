from django.db import models
from datetime import datetime

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    

class Equipamento (models.Model):
    nome = models.CharField(max_length=50)
    peso = models.FloatField()
    volume = models.FloatField()
    largura = models.FloatField()
    comprimento = models.FloatField()
    altura = models.FloatField()
    qtd_total = models.IntegerField()
    qtd_pane = models.IntegerField()
    qtd_aplicada = models.IntegerField()
    observacoes = models.TextField()
    data_atualizacao = models.DateField()
    categoria = models.ForeignKey("Categoria", on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nome
    
class Esquadrao (models.Model):
    choices = (
        ('mestre' , '1GCC'),
        ('profeta','1/1GCC'),
        ('aranha','2/1GCC'),
        ('morcego','3/1GCC'),
        ('mangrulho','4/1GCC'),
        ('zagal','5/1GCC')
    )
    
    nome = models.CharField(max_length=15, choices = choices, blank = False)
    
    def __str__(self):
        return self.nome
    