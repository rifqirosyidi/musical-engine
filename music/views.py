from django.views import generic
from .models import Album


class HomeView(generic.ListView):
    template_name = 'music/home.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    template_name = 'music/detail.html'
    model = Album

