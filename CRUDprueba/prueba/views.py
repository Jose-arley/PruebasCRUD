
from django.db.models.query_utils import FilteredRelation
from django.shortcuts import render, redirect
from django_filters.filters import DateFromToRangeFilter
from .models import Clientes
from .forms import ClientesForm
from .filters import OrderFilter
from django.forms import inlineformset_factory
from .resources import ClientesResource
from tablib import Dataset 



def clientes_list(request):

    myfilter = OrderFilter()

    context = {'clientes_list': Clientes.objects.all(), 'myfilter' : myfilter}
   
    return render(request, "clientes_list.html", context )

def clientes_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ClientesForm()
        else:
            cliente = Clientes.objects.get(pk=id)
            form = ClientesForm(instance=cliente)
        return render(request, "clientes_form.html", {'form': form},)
    else:
        if id == 0:
            form = ClientesForm(request.POST)
        else:
            cliente = Clientes.objects.get(pk=id)
            form = ClientesForm(request.POST,instance= cliente)
        if form.is_valid():
            form.save()
        return redirect('/cliente/list')


def clientes_delete(request,id):
    cliente = Clientes.objects.get(pk=id)
    cliente.delete()
    return redirect('/clientes/list')

def importar(request):  
   #template = loader.get_template('export/importar.html')  
   if request.method == 'POST':  
     cliente_resource = ClientesResource()  
     dataset = Dataset()  
     #print(dataset)  
     nuevas_cliente = request.FILES['xlsfile']  
     #print(nuevas_personas)  
     imported_data = dataset.load(nuevas_cliente.read())  
     #print(dataset)  
     result = cliente_resource.import_data(dataset, dry_run=True) # Test the data import  
     #print(result.has_errors())  
     if not result.has_errors():  
       cliente_resource.import_data(dataset, dry_run=False) # Actually import now  
   return render(request, 'importar.html') 