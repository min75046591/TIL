from django.shortcuts import render, redirect
from .forms import MovieForm, CommentForm
from .models import Movie, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies
    }
    return render(request, 'movies/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form':form,
    }
    return render(request, 'movies/create.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comments = movie.comment_set.all()
    comment_form = CommentForm()
    context = {
        'movie':movie,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request, 'movies/detail.html', context)


@login_required
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user != movie.user:
        return redirect('movies:index')
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    print(form)
    context = {
        'movie':movie,
        'form':form,
    }
    return render(request, 'movies/update.html', context)


@login_required
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.user == movie.user:
        movie.delete()
    return redirect('movies:index')


@login_required
def comments_create(request, pk):
    movie = Movie.objects.get(pk=pk)
    comments = movie.comment_set.all()
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'movie':movie,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request, 'movies/detail.html', context)


@login_required
def comments_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)