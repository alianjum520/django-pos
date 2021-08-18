from django.urls import path
from .views import list_supplier,create_supplier,update_supplier,delete_supplier

app_name = 'supplier'

urlpatterns = [
    path('list/',list_supplier,name='list'), 
    path('create/',create_supplier, name='create'),
    path('update_supplier/<str:pk>/',update_supplier,name='update_supplier'), 
    path('delete_supplier/<str:pk>/',delete_supplier, name='delete_supplier'),
]