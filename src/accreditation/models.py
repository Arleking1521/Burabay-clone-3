from django.db import models

# Create your models here.
class Accreditation(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    image = models.ImageField(upload_to='accreditation/', verbose_name='Изображение')
    file = models.FileField(verbose_name='Документ', upload_to='docs/')
    def __str__ (self) -> str:
        return f'{self.title}'

