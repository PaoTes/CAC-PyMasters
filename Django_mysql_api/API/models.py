from django.db import models

# Create your models here.
class Productos(models.Model):
        Nombre = models.CharField(max_length=100, verbose_name="Nombre")
        Descripción = models.CharField(max_length=200, verbose_name="Descripción")
        Precio = models.FloatField(verbose_name="Precio")
        Marca = models.CharField(max_length=20, verbose_name="Marca")
        Imagen = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Imagen')

        
        def _str_(self):
            return self.Nombre