from django.contrib import admin
from .models import LaborProtection
from modeltranslation.admin import TranslationAdmin
# Register your models here.

@admin.register(LaborProtection)
class LaborProtectionAdmin(TranslationAdmin):
    list_display = ( 'title', 'content')