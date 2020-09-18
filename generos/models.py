from django.db import models

class Genero(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome