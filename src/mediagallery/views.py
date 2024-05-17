from django.shortcuts import render
from .models import Mediagallery
# Create your views here.
def MediagalleryServices(request):
    file = Mediagallery.objects.all()
    return render(request, 'mediaGalleryPage/mediagallery.html', {'files':file})