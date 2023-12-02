from rest_framework import serializers
from API.models import Productos

class ProductosSerializer(serializers.ModelSerializer):

    class Meta:
        #Indico con qué modelo se va a corresponder el serializador
        model = Productos
        #listado defino  los campos de la clase productos quiero serializar
        fields = ['Nombre','Descripción','Precio','Marca','Imagen']
       