from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserCreationForm, UserProfileForm
from .models import UserProfile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Credenciales inválidas.')
            return render(request, 'accounts/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso! Has iniciado sesión automáticamente.')
            return redirect('index')
        else:
            messages.error(request, 'Hubo un error en el registro. Por favor, revisa los datos.')
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile_view(request):
    user_profile = request.user.userprofile
    context = {
        'user': request.user,
        'user_profile': user_profile,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def edit_profile_view(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado exitosamente!')
            return redirect('profile')
        else:
            messages.error(request, 'Hubo un error al actualizar tu perfil. Por favor, revisa los datos.')
    else:
        form = UserProfileForm(instance=user_profile)
    
    context = {
        'form': form
    }
    return render(request, 'accounts/edit_profile.html', context)