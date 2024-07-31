from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.



@admin.register(Science)
class ScienceAdmin(TranslationAdmin):
    list_display = ( 'title', 'addInfoTitle', 'addInfo')

@admin.register(SciencePlans)
class SciencePlansAdmin(TranslationAdmin):
    list_display = ( 'title', 'content')

@admin.register(ScienceAchievments)
class ScienceAchievmentsAdmin(TranslationAdmin):
    list_display = ( 'name',)
    
@admin.register(ScienceSovet)
class ScienceSovetAdmin(TranslationAdmin):
    list_display = ( 'title', 'description', 'creation_title', 'creation')
    
@admin.register(ScienceSovetPlans)
class ScienceSovetPlansAdmin(TranslationAdmin):
    list_display = ( 'sovet', 'title', 'document')

@admin.register(ScienceSovetMeetings)
class ScienceSovetMeetingsAdmin(TranslationAdmin):
    list_display = ( 'title', 'document') 

@admin.register(ScienceSovetRegulation)
class ScienceSovetRegulationAdmin(TranslationAdmin):
    list_display = ( 'title', 'document') 