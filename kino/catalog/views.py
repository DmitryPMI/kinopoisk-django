from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# здесь хранятся обработчики страниц

def index(response):
    return HttpResponse("<h1> Hello world! </h1>")

data = ['Форест Гамп', 'Зеленая миля']

def index1(response):
    return render(response, 'catalog/1.html', {'films': data, 'title': 'Films'})
