# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginUsuario, name='login_usuario'),
    path('register/', views.RegisterUsuario, name='register_usuario'),
    path('usuario_add/', views.UsuarioAdd, name='usuario_add'),
    path('listar_usuarios/', views.ListarUsuarios, name='listar_usuarios'),
    path('validar_usuario/', views.ValidarUsuario, name='validar_usuario'),
]
