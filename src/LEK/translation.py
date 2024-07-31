from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(LEK)
class LEKTranslationoptions(TranslationOptions):
    fields = ( 'title', 'description', 'creation_title', 'instructions','contacts','standarts')

@register(LEKPlans)
class LEKPlansTranslationoptions(TranslationOptions):
    fields = ( 'title',)

@register(LEKDocForms)
class LEKDocFormsTranslationoptions(TranslationOptions):
    fields = ( 'title',)

@register(LEKMeetings)
class LEKMeetingsTranslationoptions(TranslationOptions):
    fields = ( 'title',)

@register(LEKRegulation)
class LEKRegulationTranslationoptions(TranslationOptions):
    fields = ( 'title',)