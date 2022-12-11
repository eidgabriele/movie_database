from django import forms
from . models import Watchlist, MediaComment
from django.utils.timezone import datetime, timedelta


class WatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = ('list_owner', 'media')
        widgets = {
            'list_owner': forms.HiddenInput(),
            'media': forms.HiddenInput(),
        }

class MediaCommentForm(forms.ModelForm):
    def is_valid(self) -> bool:
        valid = super().is_valid()
        return valid
    
    class Meta:
        model = MediaComment
        fields = ('comment', 'media', 'comment_author', )
        widgets = {
            'media' : forms.HiddenInput(),
            'comment_author' : forms.HiddenInput(),
        }