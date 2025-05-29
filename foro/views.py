from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Topic, Comment
from .forms import TopicForm, CommentForm

def topic_list_view(request):
    topics = Topic.objects.all()
    context = {
        'topics': topics,
        'title': 'Foro de Conversación'
    }
    return render(request, 'foro/topic_list.html', context)

@login_required
def create_topic_view(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            messages.success(request, '¡Tu tema ha sido publicado exitosamente!')
            return redirect('foro:topic_list')
        else:
            messages.error(request, 'Hubo un error al crear tu tema. Por favor, revisa los datos.')
    else:
        form = TopicForm()
    
    context = {
        'form': form,
        'title': 'Crear Nuevo Tema'
    }
    return render(request, 'foro/create_topic.html', context)

def topic_detail_view(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    comments = topic.comments.all()
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.topic = topic
                comment.author = request.user
                try:
                    comment.save()
                    messages.success(request, '¡Tu comentario ha sido añadido!')
                    return redirect('foro:topic_detail', pk=topic.pk)
                except Exception as e:
                    messages.error(request, f'Hubo un error al añadir tu comentario: {e}. Por favor, revisa los datos.')
            else:
                messages.error(request, 'Hubo un error al añadir tu comentario. Por favor, revisa los datos.')
        else:
            messages.warning(request, 'Debes iniciar sesión para poder comentar.')
            return redirect('login')
    else:
        comment_form = CommentForm()

    context = {
        'topic': topic,
        'comments': comments,
        'comment_form': comment_form,
        'title': topic.title
    }
    return render(request, 'foro/topic_detail.html', context)