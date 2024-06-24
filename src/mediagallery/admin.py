from django.contrib import admin
from .models import Mediagallery
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.
class CustomMediagalleryAdmin(TranslationAdmin):
    fieldsets = (
        (_('Информация на русском'), {'fields': ( 'name_ru',)}),
        (_('Информация на казахском'), {'fields': ('name_kk',)}),
        (_('Информация на английском'), {'fields': ('name_en',)}),
        (None, {'fields': ('file','date')}),
    )
    add_fieldsets = (
        (_('Информация на русском'), {'fields': ( 'name_ru',)}),
        (_('Информация на казахском'), {'fields': ('name_kk',)}),
        (_('Информация на английском'), {'fields': ('name_en',)}),
        (None, {'fields': ('file',)}),
    )
    list_display = ( 'name',)

@admin.register(Mediagallery)
class MediagalleryAdmin(CustomMediagalleryAdmin):
    pass