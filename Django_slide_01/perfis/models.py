from django.db import models

# Create your models here.


# PASSO 10.1:
class Perfil:
    def __init__(self, nome='', email='', telefone='', nome_empresa=''):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nome_empresa = nome_empresa
