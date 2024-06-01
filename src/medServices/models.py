from django.db import models

# Create your models here.
class MedServices(models.Model):
    file = models.FileField(verbose_name='Файл медицинских услуг', upload_to='docs/')

    class Meta:
        verbose_name_plural = "Документы"
        verbose_name='Документ'

    def __str__(self) -> str:
        return f'Медицинские услуги'