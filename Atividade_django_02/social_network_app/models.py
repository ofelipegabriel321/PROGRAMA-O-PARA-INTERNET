from django.db import models


class Usuario(models.Model):
    email = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)
    data_de_nascimento = models.DateField()


class Perfil(models.Model):
    nome = models.CharField(max_length=30)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contatos = models.ManyToManyField('self')


class Postagem(models.Model):
    texto = models.CharField(max_length=300)
    data = models.DateField()

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)


class Comentario(models.Model):
    texto = models.CharField(max_length=100)
    data = models.DateField()

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)


class Reacao(models.Model):
    TIPOS = (
        ('C', 'CURTIR'),
        ('A', 'AMAR'),
        ('R', 'RIR'),
        ('S', 'SURPRESA'),
        ('T', 'TRISTEZA'),
        ('R', 'RAIVA')
    )

    tipo = models.CharField(max_length=1, choices=TIPOS)
    data = models.DateField()
    peso = models.IntegerField()

    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
