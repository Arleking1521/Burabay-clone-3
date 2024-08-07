from django.shortcuts import render
from .models import *
# Create your views here.

def lek(request):
    Lek = LEK.objects.order_by('id').first()
    Plans = LEKPlans.objects.order_by('id')
    Forms = LEKDocForms.objects.order_by('id')
    Regulation = LEKRegulation.objects.order_by('id')
    Meetings = LEKMeetings.objects.order_by('id')
    datas = {
        'pk': Lek.pk if Lek else None,
        'title': Lek.title if Lek else None,
        'description': Lek.description.split('\n') if Lek.description else None,
        'creation_name': Lek.creation_title if Lek else None,
        'creation': Lek.creation if Lek else None,
        'instructions': Lek.instructions.split('\n') if Lek.instructions else None, 
        'contacts': Lek.contacts.split('\n') if Lek.contacts else None, 
        'standarts': Lek.standarts.split('\n') if Lek.standarts else None, 
    }
    return render(request, 'LEK/LEK.html', {'datas':datas, 'plans':Plans, 'forms': Forms, 'regulation': Regulation, 'meetings': Meetings})

def file_detail(request, fid):
    file = LEK.objects.get(id = fid)
    return render(request, 'LEK/doc-details.html', {'file':file})

def creation_details(request, fid):
    data = LEK.objects.get(id = fid)
    file = data.creation
    return render(request, 'LEK/doc-details.html', {'file':file})

def regulation_details(request, fid):
    data = LEKRegulation.objects.get(id = fid)
    file = data.document
    return render(request, 'LEK/doc-details.html', {'file':file})

def plan_detail(request, fid):
    data = LEKPlans.objects.get(id = fid)
    file = data.document
    return render(request, 'LEK/doc-details.html', {'file':file})

def meetings_detail(request, fid):
    data = LEKMeetings.objects.get(id = fid)
    file = data.document
    return render(request, 'LEK/doc-details.html', {'file':file})

