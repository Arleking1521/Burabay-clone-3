from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(LEK)
class LEKAdmin(TranslationAdmin):
    list_display = ( 'title', 'description', 'instructions','contacts','standarts')

@admin.register(LEKPlans)
class LEKPlansAdmin(TranslationAdmin):
    list_display = ( 'title', 'document') 
                    
@admin.register(LEKDocForms)
class LEKDocFormsAdmin(TranslationAdmin):
    list_display = ( 'title', 'link')

@admin.register(LEKMeetings)
class LEKMeetingsAdmin(TranslationAdmin):
    list_display = ( 'title', 'document') 

@admin.register(LEKRegulation)
class LEKRegulationAdmin(TranslationAdmin):
    list_display = ( 'title', 'document') 