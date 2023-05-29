from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    # Salvar os dados da tela (colocadas no formulário) no banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    # Exibir todos os usuários cadastrados numa nova página. Isso deve ser feito em forma de dicionário, pois é o que o Django estabelece como padrão. 
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    # Retornar dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html',usuarios)