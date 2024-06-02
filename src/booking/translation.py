from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Booking)
class BookingTranslationoptions(TranslationOptions):
    fields = ( 'title', 'content',)
