from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name="Biografía")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ubicación")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()