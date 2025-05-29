from django import forms
from .models import Topic, Comment

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el título de tu tema'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escribe tu pregunta o historia aquí...'}),
        }
        labels = {
            'title': 'Título',
            'content': 'Contenido',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escribe tu comentario aquí...'}),
        }
        labels = {
            'content': 'Comentario',
        }