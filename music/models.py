from django.db import models


class Album(models.Model):
    album_logo = models.FileField()
    certidao_casamento = models.FileField(null=True, blank=True)


class Music(models.Model):
    nome_conjuge = models.CharField(max_length=100, null=True, blank=True)

    
