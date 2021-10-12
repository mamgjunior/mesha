from django.db import models

# Create your models here.

class Obras(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Titulo')
    editora = models.CharField(max_length=150, verbose_name='Editora')
    autor = models.CharField(max_length=200, verbose_name='Autor')
    foto = models.ImageField(upload_to='obras/img', null=True, blank=True, verbose_name='Imagem')
    criado_em = models.DateTimeField(auto_now=True, verbose_name='Criado em')

    def __str__(self) -> str:
        return self.titulo
