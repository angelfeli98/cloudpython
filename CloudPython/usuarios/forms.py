from django import forms
from django.core import validators


class UsuariosForm(forms.Form):

    user = forms.CharField(
        label = "Usuario",
        max_length = 50, 
        required=True,
        
        )
