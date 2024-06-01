from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(People)
class PeopleTranslationoptions(TranslationOptions):
    fields = ( 'post',)

@register(Doctors)
class DoctorsTranslationoptions(TranslationOptions):
    fields = ( 'title', 'content',)

@register(Teachers)
class TeachersTranslationoptions(TranslationOptions):
    fields = ( 'title', 'content',)