from django.db import models

# Create your models here.
class ScienceAchievments(models.Model):
    name = models.CharField(verbose_name='Название презентации')
    info = models.FileField(upload_to='science', verbose_name='Презентация')

    class Meta:
        verbose_name_plural = "Достижения"
        verbose_name='Достижение'

    def __str__(self) -> str:
        return f'{self.name}'
    



class Science(models.Model):
    title = models.TextField(verbose_name='Основыне пункты достижений')
    addInfoTitle = models.CharField(verbose_name='Заголовок подпунктов', blank=True)
    addInfo = models.TextField(verbose_name='Подпункты', blank=True)
    class Meta:
        verbose_name_plural = "Наукачные разработки"
        verbose_name='Информация'

    def __str__(self) -> str:
        return f'{self.title}'
    
class ScienceSovet(models.Model):
    title = models.TextField(verbose_name='Заголовок Совета')
    content = models.TextField(verbose_name='Основная информация', blank=True)
    class Meta:
        verbose_name_plural = "Научно-Технический Совет"
        verbose_name='Информация'

    def __str__(self) -> str:
        return f'{self.title}'
    
class SciencePlans(models.Model):
    title = models.TextField(verbose_name='Заголовок Совета')
    content = models.TextField(verbose_name='Основная информация', blank=True)
    class Meta:
        verbose_name_plural = "Научные планы"
        verbose_name='Информация'

    def __str__(self) -> str:
        return f'{self.title}'