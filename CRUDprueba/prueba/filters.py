from django.db.models import fields
import django_filters
from .models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model  =  Clientes
        fields = ('name_client','country','city','category')
