from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Hi Music Home")


def detail(request, album_id):
    return HttpResponse(f'The Album ID is {album_id}')