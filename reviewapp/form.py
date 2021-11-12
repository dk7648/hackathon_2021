
from django.forms import ModelForm

from reviewapp.models import Review


class ReviewCreationForm(ModelForm):

    class Meta:
        model = Review
        fields = ['rate', 'room', 'content']