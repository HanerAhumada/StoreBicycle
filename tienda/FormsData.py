import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from django import forms
from utils.Components import MultiInputForm
from utils.OwnMultiField import OwnMultiField


class formsFiltro(forms.Form):
    precio = OwnMultiField(widget_classes=[MultiInputForm],
                           propsOwn={
                            'optionGlobal': {'class': 'form-control col-md-5'}, 'cant' : 2,
                            'elementConfig': [
                                {'element': 1, 'options': {'placeholder': 'Min'}},
                                {'element': 2, 'options': {'style': 'margin-left:30px', 'placeholder': 'Max'}}
                                ]
                            }, label='Rango de precio', required=False)
    
    categoria = forms.CharField(label='Categoria', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoria', 'style': 'margin-bottom:15px'}), required=False)
    subcategoria = forms.CharField(label='Subcategoria', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subcategoria','style': 'margin-bottom:15px'}), required=False)
