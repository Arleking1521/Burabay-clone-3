from django.db import models

# Create your models here.
class OrgStruct(models.Model):
    file = models.FileField(verbose_name='Файл с изображением организационной структуры', upload_to='docs/')
    class Meta:
        verbose_name_plural = "Схема отделов"
    def __str__(self) -> str:
        return f'Организационная структура'