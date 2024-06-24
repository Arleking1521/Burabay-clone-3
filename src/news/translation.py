from modeltranslation.translator import register, TranslationOptions
from .models import Post, PostAttachment

@register(Post)
class PostTranslationoptions(TranslationOptions):
    fields = ( 'title', 'content')

