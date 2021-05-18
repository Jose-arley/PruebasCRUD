from django.shortcuts import render, redirect
from .models import Clientes
from .forms import ClientesForm


from django.http import HttpResponse


def clientes_list(request):
    context = {'clientes_list': Clientes.objects.all()}
    return render(request, "clientes_list.html", context)

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

