from django.db import models

# Create your models here.
class History(models.Model):
    title = models.CharField(verbose_name='Title')
    info = models.TextField(verbose_name='Information')

    class Meta:
        verbose_name_plural = "Истории и легенды"

    def __str__ (self) -> str:
        return f'{self.title}: {self.info}'