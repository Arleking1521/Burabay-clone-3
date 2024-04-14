from django.contrib import admin
from .models import Accreditation
from modeltranslation.admin import TranslationAdmin

# Register your models here.
@admin.register(Accreditation)
class FilesAdmin(TranslationAdmin):
    list_display = ( 'title',)