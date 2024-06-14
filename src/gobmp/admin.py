from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import GOBMP
# Register your models here.
@admin.register(GOBMP)
class GOBMPAdmin(TranslationAdmin):
    list_display = ( 'title', 'info')