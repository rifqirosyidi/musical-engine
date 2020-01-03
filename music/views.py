from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Album


# Create your views here.
def home(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/home.html', context)


def detail(request, album_id):
    # album = Album.objects.get(id=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

