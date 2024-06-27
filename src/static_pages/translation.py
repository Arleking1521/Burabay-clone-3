from modeltranslation.translator import register, TranslationOptions
from .models import index_page, openInfo

@register(index_page)
class indexPageTranslationoptions(TranslationOptions):
    fields = ( 'mission', 'view')


@register(openInfo)
class openInfoTranslationoptions(TranslationOptions):
    fields = ( 'title',)