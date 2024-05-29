from modeltranslation.translator import register, TranslationOptions
from .models import CeoDatas

@register(CeoDatas)
class CeoDatasTranslationoptions(TranslationOptions):
    fields = ( 'name', 'dateOfBirth', 'scientific', 'work', 'awards', 'sertificates', 'publications', 'positions', 'education')


