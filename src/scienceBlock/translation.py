from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(ScienceAchievments)
class ScienceInfoTranslationoptions(TranslationOptions):
    fields = ( 'name', )


@register(Science)
class ScienceTranslationoptions(TranslationOptions):
    fields = ( 'title', 'addInfoTitle', 'addInfo')

@register(ScienceSovet)
class ScienceSovetTranslationoptions(TranslationOptions):
    fields = ( 'title', 'content')


@register(SciencePlans)
class SciencePlansTranslationoptions(TranslationOptions):
    fields = ( 'title', 'content')