from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.



@admin.register(Science)
class ScienceAdmin(TranslationAdmin):
    list_display = ( 'title', 'addInfoTitle', 'addInfo')

@admin.register(ScienceSovet)
class ScienceSovetAdmin(TranslationAdmin):
    list_display = ( 'title', 'content')

@admin.register(SciencePlans)
class SciencePlansAdmin(TranslationAdmin):
    list_display = ( 'title', 'content')

@admin.register(ScienceAchievments)
class ScienceAchievmentsAdmin(TranslationAdmin):
    list_display = ( 'name',)