from django.db import models

# Create your models here.
class Accreditation(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    image = models.ImageField(upload_to='accreditation/', verbose_name='Изображение')
    file = models.FileField(verbose_name='Документ', upload_to='docs/')

    class Meta:
        verbose_name_plural = "Аккредитации"
        verbose_name='Аккредитация'

    def __str__ (self) -> str:
        return f'{self.title}'

