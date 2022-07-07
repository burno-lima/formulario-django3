from django import forms

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.CharField(label='Ida')
    data_volta = forms.CharField(label='Volta')