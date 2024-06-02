from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(ScienceInfo)
class ScienceInfoTranslationoptions(TranslationOptions):
    fields = ( 'name', )


@register(Science)
class ScienceTranslationoptions(TranslationOptions):
    fields = ( 'title', 'addInfoTitle', 'addInfo')