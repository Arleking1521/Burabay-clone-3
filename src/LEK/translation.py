from modeltranslation.translator import register, TranslationOptions
from .models import LEK, LEKPlans, LEKDocForms

@register(LEK)
class LEKTranslationoptions(TranslationOptions):
    fields = ( 'title', 'description', 'meetings', 'instructions','contacts','standarts')

@register(LEKPlans)
class LEKPlansTranslationoptions(TranslationOptions):
    fields = ( 'title',)

@register(LEKDocForms)
class LEKDocFormsTranslationoptions(TranslationOptions):
    fields = ( 'title',)
