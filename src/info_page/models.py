from django.db import models

# Create your models here.

class PacientInfo(models.Model):
    title = models.CharField(verbose_name='Title')
    info = models.TextField(verbose_name='Information')

    class Meta:
        verbose_name_plural = "Правила"

    def __str__ (self) -> str:
        return f'{self.title}: {self.info}'
    
