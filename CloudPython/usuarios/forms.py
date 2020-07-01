from django import forms
from django.core import validators


class UsuariosForm(forms.Form):

    user = forms.EmailField(
        label = "Correo electrónico:",
        max_length = 50, 
        required=True,
        )

    name = forms.CharField(
        label = "Nombre de usuario (Nickname):",
        max_length = 50, 
        required = True
    )

    password = forms.CharField(
        label = "Contraseña",
        widget = forms.PasswordInput(
            attrs = {
               "autocomplete" : "new-password"
           }
        )
    )

    conPassword  = forms.CharField(
        label = "Confirma Constraseña",
        widget = forms.PasswordInput(
            attrs = {
               "autocomplete" : "new-password"
           }
        )
    )

    image = forms.ImageField(
        label = "Escoge tu foto....",
        required= False,
        widget = forms.ClearableFileInput(
            attrs = {
               'id' : 'file'
           }
        )
    )

class LoginUser(forms.Form):
    user = forms.EmailField(
        label = "Correo:",
        max_length = 50, 
        required=True,
    )

    password = forms.CharField(
        label = "Contraseña",
        widget = forms.PasswordInput(
            attrs = {
               "autocomplete" : "new-password"
           }
        )
    )

class SendMail(forms.Form):
    user = forms.EmailField(
        label = "Correo:",
        max_length = 50, 
        required=True,
    )

class ResetPass(forms.Form):
    newpass = forms.CharField(
        label = "Nueva Contraseña",
        widget = forms.PasswordInput(
            attrs = {
               "autocomplete" : "new-password"
           }
        )
    )
    
    conPassword  = forms.CharField(
        label = "Confirma Constraseña",
        widget = forms.PasswordInput(
            attrs = {
               "autocomplete" : "new-password"
           }
        )
    )