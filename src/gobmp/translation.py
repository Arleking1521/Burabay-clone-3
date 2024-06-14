from modeltranslation.translator import register, TranslationOptions
from .models import GOBMP

@register(GOBMP)
class GOBMPTranslationoptions(TranslationOptions):
    fields = ( 'title', 'info', 'adult', 'children', 'additinaly')