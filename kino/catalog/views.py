from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Film

# здесь хранятся обработчики страниц

def index(response):
    return HttpResponse("<h1> Hello world! </h1>")

data = Film.objects.all()

def index1(response):
    return render(response, 'catalog/catalog.html', {'films': data, 'Title': 'Films'})

def base(response):
    return render(response, 'catalog/base.html', {'Title': 'Our second page'})

def film(response, film_id):
	film = Film.objects.get(id = film_id)
	return render(response, 'catalog/film.html', {'film': film})
