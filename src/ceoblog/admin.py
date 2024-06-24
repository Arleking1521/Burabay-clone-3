from django.contrib import admin
from .models import PostCeo
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.
class CustomPostCeoAdmin(TranslationAdmin):
    fieldsets = (
        (_('Автор поста'), {'fields': ('author',)}),
        (_('Информация на русском'), {'fields': ('title_ru', 'content_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'content_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'content_en',)}),
        (_('Дополнительная информация'), {'fields': ('date',)}),
    )
    add_fieldsets = (
        (_('Автор поста'), {'fields': ('author',)}),
        (_('Информация на русском'), {'fields': ('title_ru', 'content_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'content_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'content_en',)}),
    )
    list_display = ('title', 'content', 'date')

@admin.register(PostCeo)
class PostAdmin(CustomPostCeoAdmin):
    pass