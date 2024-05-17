from modeltranslation.translator import register, TranslationOptions
from .models import Mediagallery

@register(Mediagallery)
class MediagalleryTranslationoptions(TranslationOptions):
    fields = ( 'name', )

