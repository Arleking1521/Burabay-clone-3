from django.shortcuts import render
from .models import *
# Create your views here.

def booking(request):
    posts = Booking.objects.order_by('id').first()
    datas = {
        'title': posts.title if posts else None,
        'content': posts.content.split('\n') if posts else None,
    }
    return render(request, 'infoPages/booking.html', {'datas':datas})