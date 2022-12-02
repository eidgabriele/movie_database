from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'movie_app/home_page.html')

def movies(request):
    return render(request, 'movie_app/movies.html')