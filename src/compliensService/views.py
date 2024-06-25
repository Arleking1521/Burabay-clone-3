from django.shortcuts import render
from .models import *
# Create your views here.
def compServList(request):
    files = CompliensService.objects.order_by('id')
    return render(request, 'complianceService/compServiceList.html', {'files':files})

def file_detail(request, fid):
    file = CompliensService.objects.get(id = fid)
    return render(request, 'complianceService/doc-details.html', {'file':file})