from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=75)
    correo_Inst = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)    
    materias = models.ManyToManyField('Materia', related_name='profesores')
    def __str__(self):
        return self.nombre 
class Materia (models.Model):
    nombre_Materia = models.CharField(max_length=75)
    
    def __str__(self):
        return self.nombre_Materia 