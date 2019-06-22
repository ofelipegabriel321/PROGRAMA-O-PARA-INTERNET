from django.db import models


# PASSO 01, 02 E 03

#class Person(models.Model):
#    SHIRT_SIZES = (
#        ('S', 'Small'),
#        ('M', 'Medium'),
#        ('L', 'Large'),
#    )
#    name = models.CharField(max_length=30)
#    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


# PASSO 04
class Manufacter(models.Model):
    name = models.CharField(max_length=50)


class Car(models.Model):
    name = models.CharField(max_length=50)
    manufacter = models.ForeignKey(Manufacter, on_delete=models.CASCADE, related_name="cars")


# PASSO 05
class Cobertura(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class Pizza(models.Model):
    nome = models.CharField(max_length=50)
    coberturas = models.ManyToManyField(Cobertura)

    def __str__(self):
        return self.nome


# PASSO 06
class CPF(models.Model):
    numero = models.CharField(max_length = 9)

    def calcular_dv(self):
        return '00'

    def __str__(self):
        return self.numero + '-' + self.calcular_dv()


class PessoaFisica(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.OneToOneField(CPF, related_name='pessoa_fisica')

    def __str__(self):
        return self.nome


# PASSO 07
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # PASSO 07.2
    inviter = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="membership_invites")

    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

