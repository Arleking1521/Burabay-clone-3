from django.contrib import admin

from .models import Managers, Contacts, InfoAccessFaces
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.
class CustomManagersAdmin(TranslationAdmin):
    fieldsets = (
        
        (_('Информация на русском'), {'fields': ('name_ru', 'post_ru', 'reception_ru',)}),
        (_('Информация на казахском'), {'fields': ('name_kk', 'post_kk', 'reception_kk',)}),
        (_('Информация на английском'), {'fields': ('name_en', 'post_en', 'reception_en',)}),
        (_('Контактные данные'), {'fields': ('phone', 'email',)}),
        (None, {'fields': ('show',)}),
    )
    add_fieldsets = (
        (_('Информация на русском'), {'fields': ('name_ru', 'post_ru', 'reception_ru',)}),
        (_('Информация на казахском'), {'fields': ('name_kk', 'post_kk', 'reception_kk',)}),
        (_('Информация на английском'), {'fields': ('name_en', 'post_en', 'reception_en',)}),
        (_('Контактные данные'), {'fields': ('phone', 'email',)}),
        (None, {'fields': ('show',)}),
    )
    list_display = ('name', 'post',)


@admin.register(Managers)
class ManagersAdmin(CustomManagersAdmin):
    pass

class CustomContactsAdmin(TranslationAdmin):
    fieldsets = (
        (_('Информация на русском'), {'fields': ('title_ru', 'info_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'info_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'info_en',)}),
    )
    add_fieldsets = (
        (_('Информация на русском'), {'fields': ('title_ru', 'info_ru',)}),
        (_('Информация на казахском'), {'fields': ('title_kk', 'info_kk',)}),
        (_('Информация на английском'), {'fields': ('title_en', 'info_en',)}),
    )
    list_display = ( 'title', 'info')

@admin.register(Contacts)
class ContactsAdmin(CustomContactsAdmin):
    pass

class CustomInfoAccessFacesAdmin(TranslationAdmin):
    fieldsets = (
        (_('Информация на русском'), {'fields': ( 'name_ru', 'post_ru',)}),
        (_('Информация на казахском'), {'fields': ('name_kk', 'post_kk',)}),
        (_('Информация на английском'), {'fields': ('name_en', 'post_en',)}),
        (_('Контактные данные'), {'fields': ('phone', )}),
    )
    add_fieldsets = (
        (_('Информация на русском'), {'fields': ( 'name_ru', 'post_ru',)}),
        (_('Информация на казахском'), {'fields': ('name_kk', 'post_kk',)}),
        (_('Информация на английском'), {'fields': ('name_en', 'post_en',)}),
        (_('Контактные данные'), {'fields': ('phone', )}),
    )
    list_display = ( 'name', 'post')
@admin.register(InfoAccessFaces)
class InfoAccessFacesAdmin(CustomInfoAccessFacesAdmin):
    pass
