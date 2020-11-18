from django.shortcuts import render
from django.http  import HttpResponse
import requests, json

# Create your views here.
def index(request,category):
    api_key = '0f3a1533c81ff513d15f094a4169d9eb'
    url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

    req = url.format(category, api_key)
    response = requests.get(req)
    req = response.json()
    return req
    

def display(request):
    popular = index(requests,'popular')
    upcoming = index(requests,'upcoming')
    top_rated = index(requests,'top_rated')

    return render(request, 'index.html',{'popular':popular, 'upcoming':upcoming, 'top_rated': top_rated})