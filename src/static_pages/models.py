from django.db import models

class index_page(models.Model):
    bannerContent = models.TextField(verbose_name = "Текста на баннере")
    ceo_appeal = models.TextField(verbose_name="Обращение руководителя")
    class Meta:
        verbose_name_plural = "Информации"
        verbose_name='Информация'
    def __str__(self) -> str:
        return f'{self.ceo_appeal}'
    
class openInfo(models.Model):
    title = models.CharField(verbose_name='Заголовок')
    file = models.FileField(verbose_name='Документ', upload_to='docs/')
    class Meta:
        verbose_name_plural = "Приказ о прозрачности"
        verbose_name='Документ'
    def __str__(self) -> str:
        return f'{self.title}: {self.file}'