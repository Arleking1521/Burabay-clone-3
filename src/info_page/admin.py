from django.contrib import admin
from .models import PacientInfo
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.
class CustomPacientInfoAdmin(TranslationAdmin):
    fieldsets = (
        (_('Информация на русском'), {'fields': ( 'title_ru', 'info_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'info_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'info_en',)}),
    )
    add_fieldsets = (
        (_('Информация на русском'), {'fields': ( 'title_ru', 'info_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'info_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'info_en',)}),
    )
    list_display = ( 'title', 'info')
@admin.register(PacientInfo)
class PacientInfoAdmin(CustomPacientInfoAdmin):
    pass