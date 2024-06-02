from django.shortcuts import render
from .models import *
# Create your views here.
def medServices(request):
    file = MedServices.objects.order_by('-id').first()
    return render(request, 'medServices/medServices.html', {'file':file})

def medicine(request):
    posts = Medicine.objects.order_by('id').first()
    datas = {
        'title': posts.title if posts else None,
        'content': posts.content.split('\n') if posts else None,
    }
    return render(request, 'medServices/medicine.html', {'datas':datas})