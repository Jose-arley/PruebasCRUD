from django.http import HttpResponse

from import_export import resources
from .models import Clientes

class ClientesResource(resources.ModelResource):
    class Meta:
        model = Clientes

