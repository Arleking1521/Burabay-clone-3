from django.db import models

# Create your models here.
class UserFeedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Обращения"
        verbose_name='Обращение'
    def __str__(self):
        return self.name