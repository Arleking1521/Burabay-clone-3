from django.contrib import admin
from .models import StrategicDev
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(StrategicDev)
class StrategicDevAdmin(TranslationAdmin):
    list_display = ( 'name', )