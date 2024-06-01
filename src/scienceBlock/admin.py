from django.contrib import admin
from .models import *
# Register your models here.

class AddInfoAdmin(admin.ModelAdmin):
    pass

class ScienceAdmin(admin.ModelAdmin):
    filter_horizontal = ('addInfo_ru', 'addInfo_kk')  # Множественный выбор для поля Frame

admin.site.register(ScienceInfo)
admin.site.register(AddInfo, AddInfoAdmin)
admin.site.register(Science, ScienceAdmin)