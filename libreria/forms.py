from django import forms
from .models import Libro, Libro2, Libro3, Libro4, Libro5, Libro6


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'f_emision': forms.DateInput(attrs={'type': 'date'}),
            'f_envio': forms.DateInput(attrs={'type': 'date'}),

        }

class Libro2Form(forms.ModelForm):

    class Meta:
        model = Libro2
        fields = '__all__'
        widgets = {
            'f_recep': forms.DateInput(attrs={'type': 'date'}),
            'marcado': forms.CheckboxInput(),

        }

class Libro3Form(forms.ModelForm):

    class Meta:
        model = Libro3
        fields = '__all__'
        widgets = {
            'f_emision': forms.DateInput(attrs={'type': 'date'}),

        }

class Libro4Form(forms.ModelForm):

    class Meta:
        model = Libro4
        fields = '__all__'
        widgets = {
            'f_recep': forms.DateInput(attrs={'type': 'date'}),


        }

class Libro5Form(forms.ModelForm):

    class Meta:
        model = Libro5
        fields = '__all__'
        widgets = {
            'f_recep': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class Libro6Form(forms.ModelForm):

    class Meta:
        model = Libro6
        fields = '__all__'
        



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=65,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'})
    )
    password = forms.CharField(
        max_length=65,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )