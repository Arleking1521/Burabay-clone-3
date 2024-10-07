from django.contrib import admin
from .models import OrgStruct, Departments
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.
admin.site.register(OrgStruct)

class CustomDepartmentAdmin(TranslationAdmin):
    fieldsets = (
        (_('Информация на русском'), {'fields': ( 'name_ru', 'info_ru',)}),
        (_('Информация на казахском'), {'fields': ('name_kk', 'info_kk',)}),
        (_('Информация на английском'), {'fields': ('name_en', 'info_en',)}),
    )
    add_fieldsets = (
         (_('Информация на русском'), {'fields': ( 'name_ru', 'info_ru',)}),
        (_('Информация на казахском'), {'fields': ('name_kk', 'info_kk',)}),
        (_('Информация на английском'), {'fields': ('name_en', 'info_en',)}),
    )
    list_display = ( 'name', 'info',)

@admin.register(Departments)
class PostAdmin(CustomDepartmentAdmin):
    pass