from modeltranslation.translator import register, TranslationOptions
from .models import StrategicDev

@register(StrategicDev)
class ViewSovetTranslationoptions(TranslationOptions):
    fields = ( 'name', )

