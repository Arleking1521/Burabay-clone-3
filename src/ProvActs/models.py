from django.db import models

# Create your models here.
class ProvActs(models.Model):
    description = models.TextField(verbose_name = 'Описание правовых актов')
    class Meta:
        verbose_name_plural = "Акты"
        verbose_name='Акт'
    def __str__(self) -> str:
        return f'Правовые акты'