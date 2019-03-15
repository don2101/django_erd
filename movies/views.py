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
    score_data = movie_data.score_set.all()
    context = {}
    context['movie'] = movie_data
    context['scores'] = score_data

    return render(request, 'movies/detail.html', context=context)


def movie_update(request, movie_number):
    movie_data = get_object_or_404(Movie, id=movie_number)

    if request.method == 'GET':
        context = {}
        context['movie'] = movie_data
        return render(request, 'movies/update.html', context=context)
    else:
        # TODO: make update code
        return redirect('movie:movie_detail', )


def movie_delete(request, movie_number):
    movie_data = get_object_or_404(Movie, id=movie_number)
    if request.method == 'POST':
        movie_data.delete()

        return redirect('movie:movie_list')


def score_create(request, movie_number):
    movie_data = get_object_or_404(Movie, id=movie_number)

    if request.method == 'POST':
        score_data = Score()
        score = request.POST.get('score')
        content = request.POST.get('content')
        score_data.content = content
        score_data.score = score
        score_data.movie = movie_data

        score_data.save()

        return redirect('movie:movie_detail', movie_number)


def score_delete(request, movie_number, score_number):
    movie_data = get_object_or_404(Movie, id=movie_number)
    score_data = get_object_or_404(Score, id=score_number)

    if request.method == 'POST':
        score_data.delete()

        return redirect('movie:movie_detail', movie_number)

