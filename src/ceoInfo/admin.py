from django.contrib import admin
from .models import CeoDatas
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(CeoDatas)
class CeoDatasAdmin(TranslationAdmin):
    list_display = ( 'name', 'dateOfBirth', 'post', 'scientific', 'awards', 'sertificates', 'publications', 'positions', 'education')
