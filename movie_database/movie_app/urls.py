from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('movies/', views.MediaListView.as_view(), name='media_list'),
    path('movies/<int:media_id>/', views.media, name='media'),
]