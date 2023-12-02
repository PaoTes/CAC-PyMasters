
from django.urls import path, re_path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.index,name='inicio_API'),
    path('productos/', views.get_productos, name='getproductos_API'),
    path('create_producto/', views.create_producto),
    path('productos/<int:id>/', views.detail_producto),
    path('delete_producto/<int:id>/', views.delete_producto),
    path('update_producto/<int:id>/', views.update_producto)
]
   
