# accounts/admin.py
from django.contrib import admin
from .models import UserProfile 

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'location') # Campos a mostrar en la lista de perfiles
    search_fields = ('user__username', 'location') # Campos por los que se puede buscar

admin.site.register(UserProfile, UserProfileAdmin)