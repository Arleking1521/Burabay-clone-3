from django.contrib import admin
from .models import AntiCorruption
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.
class CustomAnticorruptionsAdmin(TranslationAdmin):
    fieldsets = (
        (_('Информация на русском'), {'fields': ('title_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en',)}),
        (_('Документ'), {'fields' : ('file',)}),
    )
    add_fieldsets = (
        (_('Информация на русском'), {'fields': ('title_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en',)}),
        (_('Документ'), {'fields' : ('file',)}),
    )
    list_display = ('title',)

@admin.register(AntiCorruption)
class AnticorAdmin(CustomAnticorruptionsAdmin):
    pass