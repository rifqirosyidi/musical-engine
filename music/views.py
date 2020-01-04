from django.views import generic
from django.urls import reverse_lazy
from .models import Album
from .forms import CreateUpdateAlbumForm


class HomeView(generic.ListView):
    template_name = 'music/home.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(generic.CreateView):
    form_class = CreateUpdateAlbumForm
    template_name = 'music/album_form.html'

    def get_context_data(self, **kwargs):
        kwargs['naming'] = 'Create'
        context = super(AlbumCreate, self).get_context_data(**kwargs)
        return context


class AlbumUpdate(generic.UpdateView):
    model = Album
    form_class = CreateUpdateAlbumForm
    template_name = 'music/album_form.html'

    def get_context_data(self, **kwargs):
        kwargs['naming'] = 'Update'
        context = super(AlbumUpdate, self).get_context_data(**kwargs)
        return context


class AlbumDelete(generic.DeleteView):
    model = Album
    context_object_name = 'album'
    success_url = reverse_lazy('music:home')