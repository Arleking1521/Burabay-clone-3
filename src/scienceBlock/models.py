from django.db import models

# Create your models here.
class ScienceInfo(models.Model):
    name = models.CharField(verbose_name='Название презентации')
    info = models.FileField(upload_to='science', verbose_name='Презентация')

    class Meta:
        verbose_name_plural = "Презентации"
        verbose_name='Презентация'

    def __str__(self) -> str:
        return f'{self.name}'
    
class AddInfo(models.Model):
    content = models.TextField()
    class Meta:
        verbose_name_plural = "Подпунты к основным пунктам Науке и Достижениям"
        verbose_name='Информация'

    def __str__(self) -> str:
        return f'{self.content}'


class Science(models.Model):
    title = models.CharField(verbose_name='Основыне пункты достижений')
    addInfo = models.ManyToManyField('AddInfo', related_name='science_addinfo', verbose_name='Подпункты', blank=True)
    class Meta:
        verbose_name_plural = "Наука и Достижения"
        verbose_name='Информация'

    def __str__(self) -> str:
        return f'{self.title}'