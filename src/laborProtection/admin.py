from django.contrib import admin
from .models import LaborProtection
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.
class CustomLaborProtectionAdmin(TranslationAdmin):
    fieldsets = (
        (_('Информация на русском'), {'fields': ( 'title_ru', 'content_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'content_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'content_en',)}),
    )
    add_fieldsets = (
        (_('Информация на русском'), {'fields': ( 'title_ru', 'content_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'content_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'content_en',)}),
    )
    list_display = ( 'title', 'content',)

@admin.register(LaborProtection)
class LaborProtectionAdmin(CustomLaborProtectionAdmin):
   pass