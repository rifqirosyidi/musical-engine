from django.shortcuts import render
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
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album Doesn't Exist")
    return render(request, 'music/detail.html', {'album': album})

