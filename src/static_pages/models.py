from django.db import models

class index_page(models.Model):
    bannerContent = models.TextField(verbose_name = "Текста на баннере")
    ceo_appeal = models.TextField(verbose_name="Обращение руководителя")
    class Meta:
        verbose_name_plural = "Информация"
    def __str__(self) -> str:
        return f'{self.ceo_appeal}'