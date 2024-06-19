from modeltranslation.translator import register, TranslationOptions
from .models import Managers, Contacts, InfoAccessFaces

@register(Managers)
class ManagersTranslationoptions(TranslationOptions):
    fields = ( 'name', 'post', 'reception')

@register(Contacts)
class ContactsTranslationoptions(TranslationOptions):
    fields = ( 'title', 'info')

@register(InfoAccessFaces)
class InfoAccessFacesTranslationoptions(TranslationOptions):
    fields = ( 'name', 'post')