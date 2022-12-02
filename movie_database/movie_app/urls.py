from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('movies/', views.movies, name='movies'),
]