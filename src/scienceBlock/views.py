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
    plans = ScienceSovetPlans.objects.filter(sovet_id=infos.pk)
    datas = {
        'pk': infos.pk if infos else None,
        'title': infos.title if infos else None,
        'description': infos.description if infos else None,
        'creation_name': ' '.join(infos.creation.name.split('/')[-1].split('_')).capitalize() if infos else None,
        'creation': infos.creation if infos else None,
        'regulation_name': ' '.join(infos.regulation.name.split('/')[-1].split('_')).capitalize() if infos else None,
        'regulation': infos.regulation if infos else None,
        'meetings': infos.meetings.split('\n') if infos else None, 
    }
    
    return render(request, 'sciencificBlock/scienceSovet.html', {'datas': datas, 'plans': plans})

def creation_details(request, fid):
    data = ScienceSovet.objects.get(id = fid)
    file = data.creation
    return render(request, 'sciencificBlock/doc-details.html', {'file':file})

def regulation_details(request, fid):
    data = ScienceSovet.objects.get(id = fid)
    file = data.regulation
    return render(request, 'sciencificBlock/doc-details.html', {'file':file})

def plan_detail(request, fid):
    data = ScienceSovetPlans.objects.get(id = fid)
    file = data.document
    return render(request, 'sciencificBlock/doc-details.html', {'file':file})

def sciencePlans(request):
    infos = SciencePlans.objects.order_by('id').first()
    datas = {
        'title': infos.title if infos else None,
        'content': infos.content.split('\n') if infos else None,
    }
    
    return render(request, 'sciencificBlock/sciencePlans.html', {'datas': datas})