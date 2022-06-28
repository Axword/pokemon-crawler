from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=256)
    ability = models.CharField(max_length=256, blank=True, null=True)
    species = models.CharField(max_length=256)
    defense = models.IntegerField()
