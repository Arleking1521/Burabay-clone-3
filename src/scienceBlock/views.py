from django.shortcuts import render
from .models import *
# Create your views here.

def scienceInfo(request):
    info = ScienceAchievments.objects.order_by('-id').first()

    return render(request, 'sciencificBlock/scienceAcievments.html', {'science':info})

def scienceDev(request):
    infos = Science.objects.order_by('id')
    datas = []
    for info in infos:
        data = {
            'title': info.title if info.title else None,
            'addInfoTitle': info.addInfoTitle if info.addInfoTitle else None,
            'addInfo': info.addInfo.split('\n') if info.addInfo else None,
        }
        datas.append(data)
    
    return render(request, 'sciencificBlock/scienceDev.html', {'datas': datas})


def scienceSovet(request):
    infos = ScienceSovet.objects.order_by('id').first()
    datas = {
        'title': infos.title if infos else None,
        'content': infos.content.split('\n') if infos else None,
    }
    
    return render(request, 'sciencificBlock/scienceSovet.html', {'datas': datas})

def sciencePlans(request):
    infos = SciencePlans.objects.order_by('id').first()
    datas = {
        'title': infos.title if infos else None,
        'content': infos.content.split('\n') if infos else None,
    }
    
    return render(request, 'sciencificBlock/sciencePlans.html', {'datas': datas})