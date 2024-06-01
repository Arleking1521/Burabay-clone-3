from django.db import models

# Create your models here.
class ScienceInfo(models.Model):
    name = models.CharField(verbose_name='Название презентации')
    info = models.FileField(upload_to='science', verbose_name='Презентация')

    class Meta:
        verbose_name_plural = "Презентации"
        verbose_name='Презентация'

    def __str__(self) -> str:
        return f'{self.name}'