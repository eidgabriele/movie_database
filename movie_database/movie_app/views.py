from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from . models import Media, Person

# Create your views here.

def index(request):
    return render(request,'movie_app/home_page.html')

def media(request, media_id):
    return render(request, 'movie_app/media.html', {'media': get_object_or_404(Media, id=media_id)})

class MediaListView(ListView):
    model = Media
    template_name = 'movie_app/movies.html'


