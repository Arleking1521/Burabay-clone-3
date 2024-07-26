from django.db import models

class LEK(models.Model):
    title = models.CharField(verbose_name = 'Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    creation = models.FileField(upload_to='LEK', verbose_name='Приказ о создании', blank=True)
    regulation = models.FileField(upload_to='LEK', verbose_name='Положение', blank=True)
    meetings = models.TextField(verbose_name='Заседания', blank=True)
    instructions = models.TextField(verbose_name='Инструкции по обращению', blank=True)
    contacts = models.TextField(verbose_name='Контакты секретариата', blank=True)
    standarts = models.TextField(verbose_name='Стандартные операционные процедуры', blank=True)
    class Meta:
        verbose_name_plural = "Информация"
        verbose_name='Информация'
    def __str__(self) -> str:
        return f'{self.title}'

class LEKPlans(models.Model):
    title = models.CharField(verbose_name='Название документа')
    document = models.FileField(upload_to='LEK', verbose_name='Документ', blank=True)
    class Meta:
        verbose_name_plural = "Планы ЛЭК"
        verbose_name='План'

    def __str__(self) -> str:
        return f'{self.title}'
    
class LEKDocForms(models.Model):
    title = models.CharField(verbose_name='Название формы документа')
    link = models.TextField(verbose_name='Ссылка на форму документа')
    class Meta:
        verbose_name_plural = "Формы документов"
        verbose_name='Форма'

    def __str__(self) -> str:
        return f'{self.title}'