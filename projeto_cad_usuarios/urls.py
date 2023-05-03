from app_cad_usuarios import views
from django.urls import path

urlpatterns = [
    # Rota, view responsável, nome de referência
    path('', views.home, name='home'),
    # usuarios.com/usuarios
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    # rota para listar usuarios
    path('listar-usuarios/', views.listar, name='usuarios_cadastrados'),
    # deletar usuario
    path('deletar-usuario/', views.deletar, name='excluir_usuario')

]
