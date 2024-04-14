from django.shortcuts import render
from .models import Accreditation
# Create your views here.
def accreditation_list(request):
    accreditations = Accreditation.objects.order_by('id')
    return render(request, 'accreditation/accreditation.html', {'posts':accreditations})

def accreditation_detail(request, pid):
    accreditation = Accreditation.objects.get(id = pid)
    return render(request, 'accreditation/accreditation-details.html', {'post':accreditation})