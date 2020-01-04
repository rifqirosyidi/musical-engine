from django.views import generic
from .models import Album


class HomeView(generic.ListView):
    template_name = 'music/home.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(generic.CreateView):
    model = Album
    fields = '__all__'
