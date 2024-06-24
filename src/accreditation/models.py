from django.db import models

# Create your models here.
class Accreditation(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    file = models.FileField(verbose_name='Документ', upload_to='accreditation/')
    medicine = models.BooleanField(default=False, verbose_name='Медицинская аккредитация')
    science = models.BooleanField(default=False, verbose_name='Научная аккредитация')
    type = models.CharField(max_length = 6, blank=True, null=True, verbose_name='Тип файла' )

    def save(self, *args, **kwargs):
        file_extension = self.file.name.split('.')[-1].lower()
        print(file_extension)
        if file_extension in ['jpg', 'jpeg', 'png', 'gif']:
            self.type = 'img'
        else:
            self.type = 'doc'
        
        super().save(*args, **kwargs)


    class Meta:
        verbose_name_plural = "Аккредитации"
        verbose_name='Аккредитация'

    def __str__ (self) -> str:
        return f'{self.title}'

