from modeltranslation.translator import register, TranslationOptions
from .models import CompliensService

@register(CompliensService)
class CompliensServiceTranslationoptions(TranslationOptions):
    fields = ( 'title',)
