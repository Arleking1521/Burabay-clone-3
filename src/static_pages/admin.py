from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import index_page, openInfo
# Register your models here.

@admin.register(index_page)
class indexPageAdmin(TranslationAdmin):
    list_display = ( 'bannerContent', 'ceo_appeal')

@admin.register(openInfo)
class openInfoAdmin(TranslationAdmin):
    list_display = ( 'title', 'file')