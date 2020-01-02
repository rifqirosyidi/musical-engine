from django.shortcuts import render
from django.http import HttpResponse
from .models import Album


# Create your views here.
def home(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/home.html', context)


def detail(request, album_id):
    return HttpResponse(f'The Album ID is {album_id}')