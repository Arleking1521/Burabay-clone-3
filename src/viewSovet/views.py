from django.shortcuts import render
from .models import ViewSovet
# Create your views here.

def viewSovet(request):
    files = ViewSovet.objects.order_by('id')
    return render(request, 'viewSovet/viewSovet.html', {'files':files})

def file_detail(request, fid):
    file = ViewSovet.objects.get(id = fid)
    return render(request, 'viewSovet/doc-details.html', {'file':file})
