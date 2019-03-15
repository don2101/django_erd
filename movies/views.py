from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Genre, Score


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    context = {}
    context['movies'] = movies

    return render(request, 'movies/list.html', context=context)


def movie_detail(request, movie_number):
    movie_data = get_object_or_404(Movie, id=movie_number)
    context = {}
    context['movie'] = movie_data

    return render(request, 'movies/detail.html', context=context)


def movie_update(request, movie_number):
    movie_data = get_object_or_404(Movie, id=movie_number)

    if request == 'GET':
        return render(request, 'movies/update.html')
    else:
        # TODO: make movie update code
        return redirect('movie:movie_detail')


def movie_delete(request, movie_number):
    movie_data = get_object_or_404(Movie, id=movie_number)
    if request == 'POST':
        # TODO: make movie deletion code
        return redirect('movie:movie_list')


def score_create(request):
    pass


def score_list(request):
    pass


def score_delete(request):
    pass
