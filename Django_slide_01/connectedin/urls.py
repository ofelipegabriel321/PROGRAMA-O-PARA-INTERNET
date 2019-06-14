"""connectedin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# PASSO 06.2 (PARTE 02): import das views
from perfis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # PASSO 06.2 (PARTE 01): Faça o path() com o caminho da Url (que é '') e a view,
    # que deve ser importada (OBS: nem sempre esses imports em Python são previsíveis,
    # vá tentando importar de outro modo se não conseguir no modo feito acima). Você
    # só deve usar o nome da função da view, sem os parênteses no final.
    path('', views.index),
    # PASSO 08.3: apenas a linha "path('perfil/', views.perfil)," foi feita aqui.
    # PASSO 09.1: <int:perfil_id> adicionado nesse passo e "views.perfil" substituido
    # por "views.exibir_perfil":
    path('perfil/<int:perfil_id>', views.exibir_perfil),
]
