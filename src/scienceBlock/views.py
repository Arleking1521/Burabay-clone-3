from django.shortcuts import render
from .models import *
# Create your views here.

def scienceInfo(request):
    info = ScienceInfo.objects.order_by('-id').first()

    return render(request, 'sciencificBlock/sciencificBlock.html', {'science':info})

def science(request):
    infos = Science.objects.order_by('id')
    datas = []
    for info in infos:
        data = {
            'title': info.title if info.title else None,
            'addInfoTitle': info.addInfoTitle if info.addInfoTitle else None,
            'addInfo': info.addInfo.split('\n') if info.addInfo else None,
        }
        datas.append(data)
    
    return render(request, 'sciencificBlock/achievments.html', {'datas': datas})
