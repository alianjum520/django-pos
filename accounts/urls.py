from django.urls import path,include
from .views import create_type,create_category,create_area,create,list_account,list_category,list_type,list_area,update_type,update_category,update_area,update,delete_type,delete_category,delete_area,delete

app_name='accounts'

urlpatterns = [
    path('create_type/',create_type, name='create_type'),
    path('create_category/',create_category, name='create_category'),
    path('create_area/',create_area, name='create_area'),
    path('create/',create, name='create'),
    path('list_account/',list_account, name='list_account'),
    path('list_area/',list_area, name='list_area'),
    path('list_category/',list_category, name='list_category'),
    path('list_type/',list_type, name='list_type'),
    path('update_type/<str:pk>/',update_type, name='update_type'),
    path('update_category/<str:pk>/',update_category, name='update_category'),
    path('update_area/<str:pk>/',update_area, name='update_area'),
    path('update/<str:pk>/',update, name='update'),
    path('delete_type/<str:pk>/',delete_type, name='delete_type'),
    path('delete_category/<str:pk>/',delete_category, name='delete_category'),
    path('delete_area/<str:pk>/',delete_area, name='delete_area'),
    path('delete/<str:pk>/',delete, name='delete'),
]