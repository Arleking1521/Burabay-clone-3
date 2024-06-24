from django.contrib import admin
from .models import History
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.
class CustomHistoryAdmin(TranslationAdmin):
    fieldsets = (
        (_('Информация на русском'), {'fields': ( 'title_ru', 'poem_ru', 'info_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'poem_kk', 'info_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'poem_en', 'info_en',)}),
    )
    add_fieldsets = (
        (_('Информация на русском'), {'fields': ( 'title_ru', 'poem_ru', 'info_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'poem_kk', 'info_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'poem_en', 'info_en',)}),
    )
    list_display = ( 'title', 'info')

@admin.register(History)
class HistoryAdmin(CustomHistoryAdmin):
    pass