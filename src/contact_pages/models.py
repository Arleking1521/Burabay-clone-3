from django.db import models

# Create your models here.
class Managers(models.Model):
    name = models.CharField(max_length=128, verbose_name='ФИО') 
    post = models.TextField(verbose_name='Должность')
    phone = models.CharField(verbose_name='Телефон')
    email = models.CharField(verbose_name='E-mail')
    reception = models.TextField(verbose_name='День и время приема', default = "none")
    show = models.BooleanField(verbose_name='Отображать в 2 таблицах?')

    class Meta:
        verbose_name_plural = "Руководители"

    def __str__ (self) -> str:
        return f'{self.name}: {self.post}'
    
class Contacts(models.Model):
    title = models.CharField(verbose_name='Название')
    info = models.TextField(verbose_name='Информация')

    class Meta:
        verbose_name_plural = "Контакты НИИ"

    def __str__ (self) -> str:
        return f'{self.title}: {self.info}'