from django.shortcuts import render
from django.http import HttpResponse

from .form import Movie_Form
# Create your views here.
from .models import Movie
from django.shortcuts import render, redirect

def index(request):
    movie = Movie.objects.all()
    return render(request, 'index.html', {'movie': movie})


def detail(request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        return render(request, 'detail.html', {'movie': movie})


def movie_add(request):
    if request.method == "POST":
        name = request.POST['name']
        desc = request.POST['desc']
        year=request.POST['year']
        img = request.FILES['img']
        movie = Movie(name=name,desc=desc,year=year ,img=img)
        movie.save()
    return render(request, 'add.html')



def delete(request, movie_id):
        if request.method == 'POST':
            movie = Movie.objects.get(id=movie_id)
            movie.delete()
            return redirect('/')

        return render(request, 'delete.html')

def update(request, movie_id):
            movie = Movie.objects.get(id=movie_id)
            form = Movie_Form(request.POST or None, request.FILES, instance=movie)

            if form.is_valid():
                form.save()
                return redirect('/')

            return render(request, 'update.html', {'form': form, 'movie': movie})