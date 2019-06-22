from django.db import models


# PASSO 01, 02 E 03
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


# PASSO 04
class Manufacter(models.Model):
    name = models.CharField(max_length=50)


class Car(models.Model):
    name = models.CharField(max_length=50)
    manufacter = models.ForeignKey(Manufacter, on_delete=models.CASCADE, related_name="cars")

