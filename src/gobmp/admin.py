from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import GOBMP
from django.utils.translation import gettext_lazy as _
# Register your models here.
class CustomGOBMPAdmin(TranslationAdmin):
    fieldsets = (
        (_('Информация на русском'), {'fields': ( 'title_ru', 'info_ru', 'adult_ru', 'children_ru', 'additinaly_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'info_kk', 'adult_kk', 'children_kk', 'additinaly_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'info_en', 'adult_en', 'children_en', 'additinaly_en',)}),
    )
    add_fieldsets = (
        (_('Информация на русском'), {'fields': ( 'title_ru', 'info_ru', 'adult_ru', 'children_ru', 'additinaly_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'info_kk', 'adult_kk', 'children_kk', 'additinaly_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'info_en', 'adult_en', 'children_en', 'additinaly_en',)}),
    )
    list_display = ( 'title', 'info')

@admin.register(GOBMP)
class GOBMPAdmin(CustomGOBMPAdmin):
    pass