from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Medicine)
class MedicineTranslationoptions(TranslationOptions):
    fields = ( 'title', 'content',)
