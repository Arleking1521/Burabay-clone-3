from django.contrib import admin

from .models import Managers, Contacts, InfoAccessFaces
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(Managers)
class ManagersAdmin(TranslationAdmin):
    list_display = ( 'name', 'post', 'reception')

@admin.register(Contacts)
class ContactsAdmin(TranslationAdmin):
    list_display = ( 'title', 'info')

@admin.register(InfoAccessFaces)
class InfoAccessFacesAdmin(TranslationAdmin):
    list_display = ( 'name', 'post')
