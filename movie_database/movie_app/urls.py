from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('movies/', views.MovieListView.as_view(), name='movie_list'),
    path('movies/<int:media_id>/', views.media, name='media'),
    path('series/', views.SeriesListView.as_view(), name='series_list'),
    path('companies/<int:company_id>/', views.company, name='company'),
    path('people/<int:person_id>/', views.person, name='person'),
    path('by_genre/', views.GenreListView.as_view(), name='genres'),
]