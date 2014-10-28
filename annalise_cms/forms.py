from django import forms
from django.contrib.auth.models import User

from .models import entradas, categorias

class CategoryForm(forms.ModelForm):
    class Meta:
        model = categorias

    def clean_usuario(self):
        if not self.cleaned_data['usuario']:
            return User()
        return self.cleaned_data['usuario']

class EntadasForm(forms.ModelForm):
    class Meta:
        model = entradas

    def clean_usuario(self):
        if not self.cleaned_data['usuario']:
            return User()
        return self.cleaned_data['usuario']

class indexcontactform(forms.Form):
    nombre = forms.CharField(max_length=255,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre...'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu correo...'}))
    comentario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu comentario...'}))


class ContacForm(forms.Form):
    nombre = forms.CharField(max_length=255,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre...'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu correo...'}))
    asunto = forms.CharField(max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu comentario...'}))
    mensaje = forms.CharField(max_length=255, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '8', 'placeholder': 'Tu comentario...'}))
