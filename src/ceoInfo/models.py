from django.db import models

# Create your models here.
class CeoDatas(models.Model):
    name = models.CharField(verbose_name = 'Имя руководителя')
    dateOfBirth = models.CharField(verbose_name = 'Дата рождания')
    scientific = models.TextField(verbose_name = 'Научная степень')
    positions = models.TextField(verbose_name = 'Должности')
    awards = models.TextField(verbose_name = 'Награды')
    sertificates = models.TextField(verbose_name = 'Сертификаты')
    publications = models.TextField(verbose_name = 'Публикации')
    photo = models.FileField(verbose_name= 'Фото руководителя', upload_to='images/')
    education = models.TextField(verbose_name = 'Образование')

    class Meta:
        verbose_name_plural = "Информация о руководителе"
        verbose_name='Руководитель'

    def __str__ (self) -> str:
        return f'{self.name}'
    

    
