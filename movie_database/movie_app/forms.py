from django import forms
from . models import Watchlist
from django.utils.timezone import datetime, timedelta


class WatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = ('list_owner', 'media')
        widgets = {
            'list_owner': forms.HiddenInput(),
            'media': forms.HiddenInput(),
        }