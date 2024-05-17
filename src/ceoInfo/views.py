from django.shortcuts import render

from .models import CeoDatas

# Create your views here.
def ceoInfo(request):
    datas = CeoDatas.objects.order_by('-id').first()
    
    ceo_data = {
        'name': datas.name if datas else None,
        'date_of_birth' : datas.dateOfBirth if datas else None,
        'edu_parts': datas.education.split('\n') if datas else None,
        'spec_parts':  datas.scientific.split('\n') if datas else None,
        'positions':  datas.positions.split('\n') if datas else None,
        'awards_parts':  datas.awards.split('\n') if datas else None,
        'sertif_parts':  datas.sertificates.split('\n') if datas else None,
        'public_parts':  datas.publications.split('\n') if datas else None,
        'photo': datas.photo if datas else None,
    }
    return render(request, 'ceoInfo/ceoInfoPage.html', {'datas': ceo_data})
