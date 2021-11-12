from django import forms
from django.forms import ModelForm

from boardapp import models
from reviewapp.models import Review


class ReviewCreationForm(ModelForm):

    class Meta:
        model = Review
        fields = ['content']