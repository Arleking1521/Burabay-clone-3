from django.contrib import admin
from .models import Ethica
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(Ethica)
class EthicaAdmin(TranslationAdmin):
    list_display = ( 'name', )