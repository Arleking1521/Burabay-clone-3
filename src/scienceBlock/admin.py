from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.


admin.site.register(ScienceInfo)

@admin.register(Science)
class ScienceAdmin(TranslationAdmin):
    list_display = ( 'title', 'addInfoTitle', 'addInfo')
