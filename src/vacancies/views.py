from django.shortcuts import render
from .models import Vacancies, CompetitionInfo

# Create your views here.
def VacancyInfo(request):
    infos = CompetitionInfo.objects.order_by('-id').first()
    datas = Vacancies.objects.order_by('id')
    vacancies_list = []
    for data in datas:
        requirement_parts = data.requirement.split('\n')
        vacancy_data = {
            'vacancy' : data.vacancy,
            'requirement_parts' : requirement_parts,
        }
        vacancies_list.append(vacancy_data)
    
    info = {
        'compAddress' : infos.compAddress if infos else None,
        'enterpriseAddress ': infos.enterpriseAddress if infos.enterpriseAddress else None,
        'description' : infos.description.split('\n') if infos.description else None,
        'addmisions': infos.addmisions.split('\n') if infos.addmisions else None,
        'documents': infos.documents.split('\n') if infos.documents else None,
        'additionally': infos.additionally.split('\n') if infos.additionally else None,
    }
        
    return render(request, 'infoPages/vacancyPage.html', {'datas': vacancies_list, 'info': info})
