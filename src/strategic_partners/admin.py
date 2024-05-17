from django.contrib import admin
from .models import Partners
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(Partners)
class PartnersAdmin(TranslationAdmin):
    list_display = ( 'intro', 'partners')