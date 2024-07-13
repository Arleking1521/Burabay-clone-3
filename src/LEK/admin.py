from django.contrib import admin
from .models import LEK
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(LEK)
class LEKAdmin(TranslationAdmin):
    list_display = ( 'title', )