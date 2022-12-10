from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('media_list/', views.MediaListView.as_view(), name='all_media'),
    path('media_list/<int:media_id>/', views.media, name='media'),
    path('companies/<int:company_id>/', views.company, name='company'),
    path('people/<int:person_id>/', views.person, name='person'),
    path('watchlist/', views.WatchlistView.as_view(), name='watchlist'),
    path('add_entry/<int:pk>/', views.WatchlistCreate.as_view(), name='user_watchlist_create'),
    path('delete_entry/<int:pk>/', views.WatchlistDeleteView.as_view(), 
    name='user_watchlist_delete'),
]