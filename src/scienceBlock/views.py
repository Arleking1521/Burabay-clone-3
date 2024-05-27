from django.shortcuts import render
from .models import ScienceInfo
# Create your views here.

def scienceInfo(request):
    info = ScienceInfo.objects.order_by('-id').first()

    return render(request, 'sciencificBlock/sciencificBlock.html', {'science':info})
