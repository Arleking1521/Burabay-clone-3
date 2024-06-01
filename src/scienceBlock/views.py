from django.shortcuts import render
from .models import *
# Create your views here.

def scienceInfo(request):
    info = ScienceInfo.objects.order_by('-id').first()

    return render(request, 'sciencificBlock/sciencificBlock.html', {'science':info})

def science(request):
    infos = Science.objects.all()
    
    datas = []
    for info in infos:
        addInfos = info.addInfo.all()  # Извлечение всех связанных объектов AddInfo
        
        data = {
            'title': info.title,
            'addInfo': addInfos
        }
        datas.append(data)
    
    return render(request, 'sciencificBlock/achievments.html', {'datas': datas})
