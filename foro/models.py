from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título del Tema")
    content = models.TextField(verbose_name="Contenido del Tema")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics', verbose_name="Autor")
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Publicación")

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comments', verbose_name="Tema")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="Autor")
    content = models.TextField(verbose_name="Contenido del Comentario")
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Publicación")

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return f'Comentario de {self.author.username} en {self.topic.title}'