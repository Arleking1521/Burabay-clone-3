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
    fields = ( 'title', 'description', 'creation_title')

@register(ScienceSovetPlans)
class ScienceSovetPlansTranslationoptions(TranslationOptions):
    fields = ( 'title', )

@register(ScienceSovetMeetings)
class ScienceSovetMeetingsTranslationoptions(TranslationOptions):
    fields = ( 'title', )

@register(ScienceSovetRegulation)
class ScienceSovetRegulationTranslationoptions(TranslationOptions):
    fields = ( 'title', )

@register(SciencePlans)
class SciencePlansTranslationoptions(TranslationOptions):
    fields = ( 'title', 'content')