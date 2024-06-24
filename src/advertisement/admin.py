from django.contrib import admin
from .models import Ads, Files
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.
class CustomAdsAdmin(TranslationAdmin):
    fieldsets = (
        (_('Информация на русском'), {'fields': ('title_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en',)}),
    )
    add_fieldsets = (
        (_('Информация на русском'), {'fields': ('title_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en',)}),
    )
    list_display = ('title',)

@admin.register(Ads)
class AdsAdmin(CustomAdsAdmin):
    pass

class CustomFilesAdmin(TranslationAdmin):
    fieldsets = (
        (_('Группа объявлений'), {'fields': ('ads',)}),
        (_('Информация на русском'), {'fields': ('name_ru',)}),
        (_('Информация на казахском'), {'fields': ('name_kk',)}),
        (_('Информация на английском'), {'fields': ('name_en',)}),
        (_('Документ'), {'fields' : ('file', 'type')}),
        (_('Дополнительная информация'), {'fields': ('date',)}),
    )
    add_fieldsets = (
       (_('Группа объявлений'), {'fields': ('ads',)}),
        (_('Информация на русском'), {'fields': ('name_ru',)}),
        (_('Информация на казахском'), {'fields': ('name_kk',)}),
        (_('Информация на английском'), {'fields': ('name_en',)}),
        (_('Документ'), {'fields' : ('file',)}),
    )
    list_display = ('name',)

@admin.register(Files)
class FilesAdmin(CustomFilesAdmin):
    pass