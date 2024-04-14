from modeltranslation.translator import register, TranslationOptions
from .models import Accreditation

@register(Accreditation)
class AdsTranslationoptions(TranslationOptions):
    fields = ( 'title',)