from django.db import models

class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha_creacion.strftime('%Y-%m-%d %H:%M')}"
