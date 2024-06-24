from django.contrib import admin
from .models import Accreditation
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.

   
class CustomAccreditationAdmin(TranslationAdmin):
    fieldsets = (
        (_('Информация на русском'), {'fields': ('title_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en',)}),
        (_('Документ'), {'fields': ('file', 'medicine', 'science')}),
    )
    add_fieldsets = (
        (_('Информация на русском'), {'fields': ('title_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en',)}),
        (_('Документ'), {'fields': ('file', 'medicine', 'science')}),
    )
    list_display = ( 'title',)

@admin.register(Accreditation)
class FilesAdmin(CustomAccreditationAdmin):
    pass