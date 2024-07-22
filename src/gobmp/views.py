from django.shortcuts import render
from .models import *
# Create your views here.
def gobmp(request):
    gobmp = GOBMP.objects.order_by('-id').first()
    if gobmp:
        gobmp_data = {
            'title': gobmp.title if gobmp else None,
            'info_parts': gobmp.info.split('\n') if gobmp else None,
            'adults' : gobmp.adult.split('\n') if gobmp.adult else None,
            'children' : gobmp.children.split('\n') if gobmp.children else None,
            'add' : gobmp.additinaly.split('\n') if gobmp.additinaly else None,
        }
    else:
        gobmp_data = None
    return render(request, 'infoPages/gobmp.html', {'data': gobmp_data})
