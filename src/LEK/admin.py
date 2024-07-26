from django.contrib import admin
from .models import LEK, LEKPlans, LEKDocForms
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(LEK)
class LEKAdmin(TranslationAdmin):
    list_display = ( 'title', 'description', 'meetings', 'instructions','contacts','standarts')

@admin.register(LEKPlans)
class LEKPlansAdmin(TranslationAdmin):
    list_display = ( 'title', 'document') 
                    
@admin.register(LEKDocForms)
class LEKDocFormsAdmin(TranslationAdmin):
    list_display = ( 'title', 'link')