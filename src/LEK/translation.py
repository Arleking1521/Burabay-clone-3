from modeltranslation.translator import register, TranslationOptions
from .models import LEK

@register(LEK)
class LEKTranslationoptions(TranslationOptions):
    fields = ( 'title', )

