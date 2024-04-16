import os
from django.shortcuts import render
from .models import StrategicDev
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.
def stratDev_list(request):
    posts = StrategicDev.objects.order_by('id')
    return render(request, 'strategicDevelopment/strategic_development.html', {'stratDevs':posts})

def download_file(request, sid):
    file_obj = get_object_or_404(StrategicDev, pk=sid)
    file_name = os.path.basename(file_obj.name)
    file_extension = file_obj.type
    file = f'{file_name.encode("utf-8").decode("ISO-8859-1")}.{file_extension}'
    print("file : ", file)
    response = HttpResponse(file_obj.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file}"'
    return response