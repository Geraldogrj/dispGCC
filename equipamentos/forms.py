from django import forms
from .models import Equipamento, Categoria
from tempus_dominus.widgets import DatePicker
from datetime import datetime

class FormCategoria (forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = '__all__'
        

class FormEquipamento(forms.ModelForm):
    data_atualizacao = forms.DateField(label='Data da atualização', disabled=True, initial=datetime.today())    
    class Meta:
        model = Equipamento
        fields = {'nome' , 'qtd_total' , 'qtd_pane' , 'qtd_aplicada' , 'observacoes'}
        labels = {'qtd_pane' : 'Qtd em Pane', 'observacoes' : 'Observações', 'data_atualizacao' : 'Data de Atualização'}