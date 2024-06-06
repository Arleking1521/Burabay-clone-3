from django.db import models
from django.forms import ValidationError

# Create your models here.
class Vacancies(models.Model):

    vacancy = models.TextField(verbose_name = 'Вакансия')
    requirement = models.TextField(verbose_name = 'Требования', blank=True)
    class Meta:
        verbose_name_plural = "Вакансии"
        verbose_name='Вакансия'
    def __str__ (self) -> str:
        return f'{self.vacancy}'
    
class CompetitionInfo(models.Model):
    compAddress = models.TextField(verbose_name = 'Адрес конкурса')
    enterpriseAddress = models.TextField(verbose_name = 'Адрес предприятия',  blank=True, null=True)
    description = models.TextField(verbose_name = 'Краткое описание',  blank=True, null=True)
    addmisions = models.TextField(verbose_name = 'Условия допуска к участию',  blank=True, null=True)
    documents = models.TextField(verbose_name = 'Список предоставляемсях документов',  blank=True, null=True)
    additionally = models.TextField(verbose_name = 'Дополнительная информация',  blank=True, null=True)

    class Meta:
        verbose_name_plural = "Информация о конкурсе"
        verbose_name='Информация'


