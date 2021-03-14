from django.shortcuts import render, redirect
from . forms import MovieForm
from . models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()

    return render(request, "index.html",{
        'movies' :movies
    })

def show(request):
    pass

def create(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request, "netflix/create.html",{
        'form' : form
    })

def update(request, id):
    movie = movie.objects.get(pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance = movie)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request, "netflix/edit.html",{
        'form' : form,
        'movie': movie
    })

def delete(request):
    pass