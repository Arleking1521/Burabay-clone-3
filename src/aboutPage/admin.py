from django.contrib import admin
from .models import AboutInfo
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.

   
class CustomAboutAdmin(TranslationAdmin):
    fieldsets = (
        (_('Информация на русском'), {'fields': ('About_ru', 'LDO_ru')}),
        (_('Информация на казахском'), {'fields': ('About_kk', 'LDO_kk')}),
        (_('Информация на английском'), {'fields': ('About_en', 'LDO_en')}),
        (_('Документ'), {'fields': ('file',)}),
    )
    add_fieldsets = (
        (_('Информация на русском'), {'fields': ('About_ru', 'LDO_ru')}),
        (_('Информация на казахском'), {'fields': ('About_kk', 'LDO_kk')}),
        (_('Информация на английском'), {'fields': ('About_en', 'LDO_en')}),
        (_('Документ'), {'fields': ('file',)}),
    )
    list_display = ('About_ru', 'LDO_ru', 'About_kk', 'LDO_kk', 'About_en', 'LDO_en', 'file')

@admin.register(AboutInfo)
class AboutInfoAdmin(CustomAboutAdmin):
    pass