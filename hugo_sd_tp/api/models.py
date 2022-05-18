from django.db import models

# Create your models here.
class Artigo(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    autor = models.CharField(max_length=80)
    anoPublicacao = models.CharField(max_length=4)
    url = models.CharField(max_length=2048)

    def __str__(self):
        return self.titulo

