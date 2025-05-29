from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'birth_date', 'location']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'bio': 'Biografía',
            'birth_date': 'Fecha de Nacimiento',
            'location': 'Ubicación',
        }