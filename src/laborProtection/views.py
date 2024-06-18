from django.shortcuts import render
from .models import LaborProtection
# Create your views here.
def laborProtection(request):
    data = LaborProtection.objects.order_by('-id').first()
    datas = {
        'title': data.title if data else None,
        'content': data.content.split('\n') if data else None,
    }
    return render(request, 'infoPages/laborProtection.html', {'data': datas})