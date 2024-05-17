from modeltranslation.translator import register, TranslationOptions
from .models import Partners

@register(Partners)
class PartnersTranslationoptions(TranslationOptions):
    fields = ('intro', 'partners')


