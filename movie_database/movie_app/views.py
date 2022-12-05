from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from . models import Media, Person

# Create your views here.

def index(request):
    return render(request,'movie_app/home_page.html')

def media(request, media_id):
    return render(request, 'movie_app/media.html', {'media': get_object_or_404(Media, id=media_id)})

class MovieListView(ListView):
    model = Media
    template_name = 'movie_app/media_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_series=False).order_by('release_date')
        return queryset

class SeriesListView(ListView):
    model = Media
    template_name = 'movie_app/media_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_series=True).order_by('release_date')
        return queryset