from modeltranslation.translator import register, TranslationOptions
from .models import Departments

@register(Departments)
class PostTranslationoptions(TranslationOptions):
    fields = ( 'name', 'info')

