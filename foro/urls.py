from django.urls import path
from . import views

urlpatterns = [
    path('guardar_comentario/', views.guardar_comentario, name='guardar_comentario'),
]
