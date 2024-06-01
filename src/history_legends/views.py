from django.shortcuts import render
from .models import History

# Create your views here.

def history_list(request):
    history = History.objects.order_by('-id').first()
    history_data = {
        'title': history.title if history else None,
        'poem': history.poem.split('\n') if history else None,
        'info_parts': history.info.split('\n') if history else None,
    }
    return render(request, 'infoPages/historyPage.html', {'history': history_data})
