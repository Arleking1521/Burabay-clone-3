from django.shortcuts import render
from .models import LEK
# Create your views here.

def lek(request):
    files = LEK.objects.order_by('id')
    return render(request, 'LEK/LEK.html', {'files':files})

def file_detail(request, fid):
    file = LEK.objects.get(id = fid)
    return render(request, 'LEK/doc-details.html', {'file':file})

