from django.db import models


class Objet(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.IntegerField()
