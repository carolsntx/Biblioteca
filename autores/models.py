from django.db import models

class Autor(models.Model):
    codigo = models.IntegerField()
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
