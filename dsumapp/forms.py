from django.forms import ModelForm

from dsumapp.models import Dsum


class DsumCreationForm(ModelForm):
    class Meta:
        model = Dsum
        fields = ['title', 'content']