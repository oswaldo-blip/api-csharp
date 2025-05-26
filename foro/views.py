from django.http import JsonResponse
from .models import Comentario

def guardar_comentario(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        mensaje = request.POST.get("mensaje")
        if nombre and mensaje:
            comentario = Comentario.objects.create(nombre=nombre, mensaje=mensaje)
            return JsonResponse({
                'nombre': comentario.nombre,
                'mensaje': comentario.mensaje,
                'fecha': comentario.fecha_creacion.strftime("%Y-%m-%d %H:%M")
            })
    return JsonResponse({"error": "Datos inválidos"}, status=400)
