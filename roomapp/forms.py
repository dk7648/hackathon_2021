from django.forms import ModelForm

from roomapp.models import Room


class RoomCreationForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name']