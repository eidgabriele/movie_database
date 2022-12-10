from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from . models import Media, Person, Company, Genre, Watchlist, Location
from django.views.generic.edit import FormMixin
from django.db.models import Q
from . forms import WatchlistForm


def index(request):
    return render(request,'movie_app/home_page.html')

def media(request, media_id):
    return render(request, 'movie_app/media.html', {'media': get_object_or_404(Media, id=media_id)})

def company(request, company_id):
    return render(request, 'movie_app/company.html', {'company': get_object_or_404(Company, id=company_id)})

def person(request, person_id):
    return render(request, 'movie_app/person.html', {'person': get_object_or_404(Person, id=person_id)})

class MediaListView(ListView):
    model = Media
    template_name = 'movie_app/media_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
            Q(name__icontains=search) | 
            Q(cast_crew__person__first_name__icontains=search) |
            Q(cast_crew__person__last_name__icontains=search))
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

class WatchlistView(LoginRequiredMixin, ListView):
    model = Watchlist
    template_name = 'movie_app/user_watchlist.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(list_owner=self.request.user).order_by('date_added')
        return queryset
    

class WatchlistCreate(LoginRequiredMixin, CreateView):
    model = Watchlist
    form_class = WatchlistForm
    template_name = 'movie_app/user_watchlist_add.html'

    def form_valid(self, form):
        form.instance.list_owner = self.request.user
        form.instance.media = Media.objects.get(pk=self.kwargs['pk'])
        messages.success(self.request, f'{form.instance.media.name} was added to your watchlist!')
        return super().form_valid(form)

    def get_success_url(self):
        id = self.kwargs['pk']
        return reverse_lazy('media', kwargs={'media_id': id })


class WatchlistDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Watchlist
    template_name = 'movie_app/user_watchlist_delete.html'
    success_url = reverse_lazy('watchlist')

    def test_func(self):
        watchlist_entry = self.get_object()
        return self.request.user == watchlist_entry.list_owner

    def form_valid(self, form):
        watchlist_entry = self.get_object()
        return super().form_valid(form)
