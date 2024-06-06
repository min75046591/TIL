from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie, Genre
from django.http import JsonResponse

# Create your views here.
@require_safe
def index(request):
    print(request.GET)
    movies = Movie.objects.all()
    genres= Genre.objects.all()
    context={
        'movies':movies,
        'genres':genres
    }
    return render(request,'movies/index.html',context)


def filter_genre(request):
    genre_name = request.GET.get('genre')
    if genre_name == 'none':
        print(genre_name)
        filtered_movies = Movie.objects.all()
        print(filtered_movies)
    else:
        genre = Genre.objects.get(name=genre_name)
        filtered_movies = genre.movie_set.all()
    # print(filtered_movies)
    # for movie in filtered_movies:
    #     print(movie.title)

    movies_list = []
    for movie in filtered_movies:
        movies_list.append(movie.title)
    print(movies_list)
    context = {
        'movies_list' : movies_list
    }
    return JsonResponse(context)
    # return render(request,'movies/index.html')


@require_safe
def recommended(request):
    pass
