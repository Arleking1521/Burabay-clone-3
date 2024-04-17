from modeltranslation.translator import register, TranslationOptions
from .models import Ethica

@register(Ethica)
class EthicaTranslationoptions(TranslationOptions):
    fields = ( 'name', )

