from django.shortcuts import render

# first view created

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")