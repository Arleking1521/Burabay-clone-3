from django.contrib import admin
from .models import Mediagallery
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(Mediagallery)
class MediagalleryAdmin(TranslationAdmin):
    list_display = ( 'name',)