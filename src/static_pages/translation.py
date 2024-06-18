from modeltranslation.translator import register, TranslationOptions
from .models import index_page, openInfo

@register(index_page)
class indexPageTranslationoptions(TranslationOptions):
    fields = ( 'bannerContent', 'ceo_appeal')


@register(openInfo)
class openInfoTranslationoptions(TranslationOptions):
    fields = ( 'title',)