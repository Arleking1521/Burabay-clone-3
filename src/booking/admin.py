from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Booking)
class BookingAdmin(TranslationAdmin):
    list_display = ( 'title', 'content')