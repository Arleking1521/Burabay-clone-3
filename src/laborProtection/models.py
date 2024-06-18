from django.db import models

# Create your models here.
class LaborProtection(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    class Meta:
        verbose_name_plural = "Информации"
        verbose_name='Информация'

    def __str__ (self) -> str:
        return f'{self.title}'