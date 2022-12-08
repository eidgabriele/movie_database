from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('media_list/', views.MediaListView.as_view(), name='media_list'),
    path('media_list/<int:media_id>/', views.media, name='media'),
    path('companies/<int:company_id>/', views.company, name='company'),
    path('people/<int:person_id>/', views.person, name='person'),
    path('watchlist/', views.WatchlistView.as_view(), name="watchlist"),
    # path('by_genre/', views.MediaListView.as_view(), name='genres'),
]