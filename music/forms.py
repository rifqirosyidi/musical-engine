from django.forms import ModelForm, FileInput
from .models import Album


class CreateUpdateAlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_logo': FileInput(attrs={'class': 'btn blue-grey darken-4', }),
        }
