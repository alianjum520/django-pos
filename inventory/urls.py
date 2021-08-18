from django.urls import path,include
from .views import create_product,list_products,update_products,delete_products,create_category,list_category,delete_category,update_category
app_name='inventory'

urlpatterns = [
   path('list/',list_products,name='list'), 
   path('create/',create_product, name='create'),
   path('list_category/',list_category,name='list_category'), 
   path('create_category/',create_category, name='create_category'),
   path('update_category/<str:pk>/',update_category, name='update_category'),
   path('delete_category/<str:pk>/',delete_category, name='delete_category'),
   path('update_products/<str:pk>/',update_products, name='update_products'),
   path('delete_products/<str:pk>/',delete_products, name='delete_products'),
]