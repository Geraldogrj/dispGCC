from django import forms
from .models import Equipamento, Categoria

class FormCategoria (forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = '__all__'

class FormEquipamento(forms.ModelForm):
    
    class Meta:
        model = Equipamento
        fields = '__all__'