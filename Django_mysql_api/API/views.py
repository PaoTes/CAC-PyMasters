from django.shortcuts import render
from django.http import HttpResponse
#importo el modelo de Productos
from API.models import Productos
#importo el serializador creado
from API import serializers
#importo funcionalidades de la librería rest_framework
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hola Mundo Django</h1>')


    @api_view(['GET']) #solo puede ser accedido si el metodo es get
    def get_productos(request):
        """
        Lista todos los productos
        """
    #se buscan todos los registros guardados en la base
    productos = Productos.object.filter()
    
    serializer = serializer.ProductosSerializer(productos, many=True)

    return Response(serializer.data)

    @api_view(['POST'])
    def create_producto(request):
        """
        Crear un producto
        """
    #Se serializa los datos recibidos desde el formulario
    serializer = serializers.ProductosSerializer(data=request.data)
    #Se ejecutan las validaciones
    if serializer.is_valid():
        #Se registra en base de datos
        serializer.save()
        #Se genera la respuesta
        response = {'status':'Ok',
                    'message':'Producto creado exitosamente',
                    'data':serializer.data}
        return Response(data= response, status=status.HTTP_201_CREATED)
        response = {'status':'Error',
                'message':'No se pudo crear el producto',
                'errors':serializer.errors}
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def detail_producto(request, id):
        """
        Muestra un producto según id.
        """
    try:
        #Se busca el producto en la base por el id
        productos = Productos.objects.get(pk=id)
    except Productos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')

    serializer = serializers.ProductosSerializer(producto)
    return Response(serializer.data)

    @api_view(['DELETE'])
    def delete_movie(request, id):
        """
        Eliminar un producto segun id.
        """
    try:
        #Se busca el producto de la base por el id
        productos = Productos.objects.get(pk=id)        
    except Productos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')
    #elimina el registro de la base de datos
    productos.delete()
    return Response({'message':'Se eliminó el producto'},status=status.HTTP_200_OK)


    @api_view(['PUT'])
    def update_producto(request, id):
        """
        Actualiza un producto
        """
    try:
       productos = Productos.objects.get(pk=id)
    except Productos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')
    
    #Se realiza proceso de serializacion, con el producto encontrado
    # y los datos que fueron enviados desde el cliente
    serializer = serializers.ProductosSerializer(productos, data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {'status':'Ok',
                    'message':'Producto modificado exitosamente',
                    'data':serializer.data}
        return Response(data=response)
        response = {'status':'Error',
                'message':'No se pudo modificar el producto',
                'errors':serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)