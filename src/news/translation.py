from modeltranslation.translator import register, TranslationOptions
from .models import Post, PostAttachment

@register(Post)
class PostTranslationoptions(TranslationOptions):
    fields = ( 'title', 'content')

@register(PostAttachment)
class PostAttachmentAdmin(TranslationOptions):
    fields = ('file', 'post', 'type')