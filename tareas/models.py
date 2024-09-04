from django.db import models

# Create your models here.
class Tarea (models.Model):
    estado= [('completo','Finalizado'),('incompleto','pendiente')]
    titulo= models.CharField(max_length=150)
    descripcion=models.TextField(max_length=500)
    estados= models.CharField(max_length=20,choices=estado,default='incompleto')
    def __str__(self):
        return self.titulo 