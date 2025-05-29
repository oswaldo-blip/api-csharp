from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
]