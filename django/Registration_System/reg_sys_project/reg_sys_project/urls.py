from django.urls import path
from app_reg_sys import views

urlpatterns = [
    path('',views.home, name='home'),
    path('usuarios/', views.usuarios,name='listagem_usuarios')
]
