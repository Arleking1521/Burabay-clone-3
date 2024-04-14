from django.shortcuts import render
from .models import Managers, Contacts
# Create your views here.

def managerPostList(request):
    managers = Managers.objects.order_by('id')
    contacts = Contacts.objects.order_by('id')
    return render(request, 'infoPages/contacts.html', {'managers': managers, 'contacts': contacts})
