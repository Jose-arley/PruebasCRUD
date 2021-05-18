from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.clientes_form,name='clientes_insert'), # get and post req. for insert operation
    path('<int:id>/', views.clientes_form,name='clientes_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.clientes_delete,name='clientes_delete'),
    path('list/',views.clientes_list,name='clientes_list'), # get req. to retrieve and display all records
    path('load/',views.importar,name='clientes_load') # get req. to retrieve and display all records
]