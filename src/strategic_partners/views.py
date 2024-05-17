from django.shortcuts import render

from .models import Partners

# Create your views here.
def strategicPartners(request):
    datas = Partners.objects.order_by('-id').first()
    
    partners_data = {
        'intro': datas.intro if datas else None,
        'partners' : datas.partners.split('\n') if datas else None,
    }
    return render(request, 'strategic_partners/strategicPartners.html', {'datas': partners_data})