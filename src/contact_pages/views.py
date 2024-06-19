from django.shortcuts import render
from .models import Managers, Contacts, InfoAccessFaces
# Create your views here.

def managerPostList(request):
    managers = Managers.objects.order_by('id')
    contacts = Contacts.objects.order_by('id')
    infoAccess = InfoAccessFaces.objects.order_by('id')
    return render(request, 'infoPages/contacts.html', {'managers': managers, 'contacts': contacts, 'infoAccess': infoAccess})
