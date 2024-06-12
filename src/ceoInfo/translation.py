from modeltranslation.translator import register, TranslationOptions
from .models import CeoDatas

@register(CeoDatas)
class CeoDatasTranslationoptions(TranslationOptions):
    fields = ( 'name', 'dateOfBirth', 'post', 'scientific', 'work', 'awards', 'sertificates', 'publications', 'positions', 'education')


