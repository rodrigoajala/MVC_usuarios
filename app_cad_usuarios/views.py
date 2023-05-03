from django.shortcuts import render

from .models import Usuario


# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html')


def usuarios(request):
    # Salvar os dados da tela para o banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Exibir todos os dados do usario ja cadastrados na tela.
    usuarios = {
        'usuarios': Usuario.objects.all()

    }

    # Retornar os dados para a pagina de usuarios.
    return render(request, 'usuarios/usuarios.html', usuarios)


def listar(request):
    usuarios = {
        'usuarios': Usuario.objects.all()

    }

    # Retornar os dados para a pagina de usuarios.
    return render(request, 'usuarios/usuarios.html', usuarios)


def deletar(request):
    # Salvar os dados da tela para o banco de dados.
    id_del = request.POST.get('id_usuario')
    Usuario.objects.filter(id_usuario=id_del).delete()

    todos_usuarios = {
        'usuarios': Usuario.objects.all()

    }

    # Retornar os dados para a pagina de usuarios.
    return render(request, 'usuarios/usuarios.html', todos_usuarios)
