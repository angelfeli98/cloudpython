from django import forms
from django.core import validators
from ckeditor.fields import CKEditorWidget 
from datetime import datetime
from proyectos.models import Category

class ProyectoSave(forms.Form):

    public_options = [(res.id, res.name) for res in Category.objects.all()]

    name = forms.CharField(
        label = 'Nombre del proyecto',
        max_length = 50, 
        required = True
    )

    category = forms.TypedChoiceField(
        label = 'Categoria del proyecto',
        choices = public_options
    )

    goal = forms.IntegerField(
        label = 'Meta del proyecto $',
        required = True,
    )

    deadline = forms.DateTimeField(
        label = 'Fecha limite',    
        required = False,
        widget = forms.TimeInput(
            attrs = {
               'type' : 'date'
           }
        )
    )

    description = forms.CharField(
        label = 'Cuentanos de tu proyecto',
        max_length = 10000, 
        required = True,
        widget = CKEditorWidget()
    )

    image = forms.ImageField(
        label = 'Carga la imagen...',        
        required = True,
        widget = forms.ClearableFileInput(
            attrs = {
               'id' : 'file'
           }
        )
    )


