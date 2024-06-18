from modeltranslation.translator import register, TranslationOptions
from .models import LaborProtection

@register(LaborProtection)
class LaborProtectionTranslationoptions(TranslationOptions):
    fields = ( 'title', 'content')