from django.db import models

# Create your models here.
class Livros(models.Model):
    codigo = models.IntegerField(default=0)
    nome = models.CharField(max_length=30)
    def __str__(self):
        return self.nome
