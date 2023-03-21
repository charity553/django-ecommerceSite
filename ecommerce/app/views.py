from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# Create a simple view to set up the app
def home(req):
    return HttpResponse("Hello")
