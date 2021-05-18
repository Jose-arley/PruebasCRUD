from django import forms
from django.db.models import fields
from django.forms.widgets import PasswordInput
from .models import *

class ClientesForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ('name_client','country','city','category')
        labels = {
            'name_client':'Name client',
            'category':'Category'
        }

    def __init__(self, *args, **kwargs):
        super(ClientesForm,self).__init__(*args, **kwargs)
        self.fields['country'].empty_label = "Select"
        self.fields['city'].required = False