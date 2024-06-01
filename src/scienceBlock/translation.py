from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(ScienceInfo)
class ScienceInfoTranslationoptions(TranslationOptions):
    fields = ( 'name', )

@register(AddInfo)
class AddInfoTranslationoptions(TranslationOptions):
    fields = ( 'content', )

@register(Science)
class ScienceTranslationoptions(TranslationOptions):
    fields = ( 'title', 'addInfo')