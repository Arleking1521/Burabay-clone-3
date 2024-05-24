from django.db import models

# Create your models here.
class AntiCorruption(models.Model):
    title = models.CharField(verbose_name = 'Название')
    file = models.FileField(verbose_name='Файл', upload_to='docs/')
    
    class Meta:
        verbose_name_plural = "Противодействие коррупции"

    def __str__(self) -> str:
        return f'{self.title}: {self.file}'
