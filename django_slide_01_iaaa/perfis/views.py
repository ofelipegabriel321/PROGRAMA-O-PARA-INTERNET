from django.shortcuts import render
# PASSO 07.2 COMENTOU:
# from django.http import HttpResponse
# PASSO 10.2 (PARTE 01):
from perfis.models import Perfil

# Create your views here.


# PASSO 06.1: Criando a função/view index, observe que ela DEVE receber o parâmentro
# request. Nesse caso estamos retornando uma response com o método HttpResponse(),
# que precisa ser importado de django.http :
def index(request):
    # PASSO 07.2 COMENTOU:
    # return HttpResponse('Bem-vindo ao Connectedin')

    # PASSO 07.2: método render(), que tem como argumentos a request (o parâmentro
    # da view) e o nome do template ("index.html" no caso).
    return render(request, 'index.html')


# PASSO 08.2: Criando a view, por enquanto só com a linha "return render(request,
# 'perfil.html')"
# PASSO 09.2 COMENTOU:
# def perfil(request):
#     return render(request, 'perfil.html')

# PASSO 09.2: Tem apenas as linas "print('Id do perfil recebido: {}'.format(perfil_id))"
# e "return render(request, 'perfil.html')"
# PASSO 10.2: fazendo as 2 possibilidades perfis e adicionando um atributo no render.
# Esse atributo será recebido pela página Html com o nome pelo qual está sendo passado.
def exibir_perfil(request, perfil_id):
    print('Id do perfil recebido: {}'.format(perfil_id))
    perfil = Perfil()
    if perfil_id == 1:
        perfil = Perfil('Elvis', 'elvis@gmail.com', '99999-9999', 'IFPI')
    if perfil_id == 2:
        perfil = Perfil('Lucas', 'lucas@gmail.com', '99987-4567', 'TCE')
    return render(request, 'perfil.html', {"perfil": perfil})
