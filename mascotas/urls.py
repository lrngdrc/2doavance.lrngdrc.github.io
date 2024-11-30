from django.urls import path
from . import views

urlpatterns = [
    path('', views.Razas, name='Razas'),
    path('Bienvenida/', views.Bienvenida, name='Bienvenida'),
    ]