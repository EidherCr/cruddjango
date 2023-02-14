from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['Titulo', 'Descripcion', 'Importante']
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe un titulo'}),
            'Descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe un descripción'}),
            'Importante': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
