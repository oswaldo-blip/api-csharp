from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Ahora el index es la página principal
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # login accesible desde botón

    # Agregado: logout por enlace GET
    path('logout/', views.logout_view, name='logout-link'),
    path('accounts/', include('accounts.urls')),

    path('nosotros/', views.nosotros, name='nosotros'),
    path('contenido/', views.contenido, name='contenido'),
    
    # Ambas rutas se mantienen como pediste
    path('foro/', views.foro, name='foro'),
    path('foro/', include('foro.urls')),  

    path('encuesta/', views.encuesta, name='encuesta'),
]

