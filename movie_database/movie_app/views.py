from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib import messages
from . models import Media, Person, Company, Genre
from django.views.generic.edit import FormMixin

# Create your views here.

def index(request):
    return render(request,'movie_app/home_page.html')

def media(request, media_id):
    return render(request, 'movie_app/media.html', {'media': get_object_or_404(Media, id=media_id)})

class MediaListView(ListView):
    model = Media
    template_name = 'movie_app/media_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get("is_series") != None:
            queryset = queryset.filter(is_series=self.request.GET.get("is_series"))
        genre_id = self.request.GET.get('genre_id')
        if genre_id:
            queryset = queryset.filter(genre__id=genre_id)
        return queryset.order_by('release_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre_id = self.request.GET.get('genre_id')
        context['genres'] = Genre.objects.all()
        if genre_id:
            context['genre'] = get_object_or_404(Genre, id=genre_id)
        return  context

def company(request, company_id):
    return render(request, 'movie_app/company.html', {'company': get_object_or_404(Company, id=company_id)})

def person(request, person_id):
    return render(request, 'movie_app/person.html', {'person': get_object_or_404(Person, id=person_id)})

# class GenreListView(ListView):
#     model = Media
#     template_name = 'movie_app/by_genre.html'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         genre_id = self.request.GET.get('genre_id')
#         if genre_id:
#             queryset = queryset.filter(genre__id=genre_id)
#         return queryset
    
