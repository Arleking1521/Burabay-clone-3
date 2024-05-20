from django.contrib import admin
from .models import Post, PostAttachment
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ( 'title', 'content', 'date')
    fields = ('author', 'title', 'date', 'content')

@admin.register(PostAttachment)
class PostAttachmentAdmin(TranslationAdmin):
    list_display = ( 'file', 'post', 'type')
    fields = ('file', 'post', 'type')