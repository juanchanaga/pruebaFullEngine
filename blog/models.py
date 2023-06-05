from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blogs(models.Model):
    titulo = models.CharField(max_length=250)
    contenido = models.TextField(max_length=1500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

class Comentarios(models.Model):
    comentario = models.TextField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
