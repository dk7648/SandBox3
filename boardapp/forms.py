from django import forms
from django.forms import ModelForm

from boardapp import models
from boardapp.models import Board


class BoardCreationForm(ModelForm):
    #type = forms.ModelChoiceField(queryset=Board.objects.all(), required=False)

    class Meta:
        model = Board
        fields = ['title', 'type', 'content']