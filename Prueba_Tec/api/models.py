from django.db import models
from django.contrib.auth.models import User




class libro(models.Model):
    titulo = models.CharField( max_length=50, null= False)
    autor = models.CharField( max_length=50,null= False)
    disponible = models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} - {'Disponible' if self.disponible else 'No disponible'}"

    
class prestamo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(libro, on_delete=models.CASCADE)
    fecha = models.DateField()
    fecha_devolucion = models.DateField()
   

    def __str__(self):
     return f"{self.usuario.username} - {self.libro.titulo} - {self.fecha} - {self.fecha_devolucion}"

    
    
    
    

