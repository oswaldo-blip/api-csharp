from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.decorators.http import require_GET

# Vistas principales
def index(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def contenido(request):
    return render(request, 'core/contenido.html')

def foro(request):
    return render(request, 'core/foro.html')

def encuesta(request):
    return render(request, 'core/encuesta.html')

# Vista de logout por GET para usar como enlace simple
@require_GET
def logout_view(request):
    logout(request)
    return redirect('index')  # Puedes redirigir a cualquier otra vista
