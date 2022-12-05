from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib import messages
from . models import Media, Person, Company
from django.views.generic.edit import FormMixin

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

def company(request, company_id):
    return render(request, 'movie_app/company.html', {'company': get_object_or_404(Company, id=company_id)})

def person(request, person_id):
    return render(request, 'movie_app/person.html', {'person': get_object_or_404(Person, id=person_id)})

# class CompanyListView(ListView):
#     model = Company
#     template_name = 'movie_app/company.html'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(company=self.name).order_by('release_date')
#         return queryset 