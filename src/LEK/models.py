from django.db import models

class LEK(models.Model):
    title = models.CharField(verbose_name = 'Название')
    file = models.FileField(verbose_name='Документ', upload_to='docs/')
    class Meta:
        verbose_name_plural = "Публикации"
        verbose_name='Публикация'
    def __str__(self) -> str:
        return f'{self.title}: {self.file}'
