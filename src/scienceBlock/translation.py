from modeltranslation.translator import register, TranslationOptions
from .models import ScienceInfo

@register(ScienceInfo)
class ScienceInfoTranslationoptions(TranslationOptions):
    fields = ( 'name', )

