from datetime import date
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello django!</h1>')

def about(request):
    return HttpResponse('<h1>Bienvenue nous allons parler de nous.')

def listings(request):
    return HttpResponse('<h1>Cette page présente la liste des annonces<h1>')

def contact_us(request):
    return HttpResponse('<h1>Bienvenue sur notre page de contact')

def indexl(request):
    return render(request, "index.html")

