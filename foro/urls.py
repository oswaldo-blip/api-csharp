from django.urls import path
from . import views

app_name = 'foro'

urlpatterns = [
    path('', views.topic_list_view, name='topic_list'),
    path('crear/', views.create_topic_view, name='create_topic'),
    path('<int:pk>/', views.topic_detail_view, name='topic_detail'),
]