from django.db import models

# Create your models here.

class Partners(models.Model):
    intro = models.TextField(verbose_name = 'Введение')
    partners = models.TextField(verbose_name='Список партнеров')
    def __str__ (self) -> str:
        return f'strategic partners'