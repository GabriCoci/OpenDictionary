from django.shortcuts import render
from django.http import HttpResponse
from .tests import dictionary

# Create your views here.
def home_view(request):
    return render(request, "home.html", {})


def myView(request):
   
    dictionary(request)

    return render(request, 'final.html', dictionary(request))
    
def err404_view(request, exception):
    return render(request, '404.html')


def err500_view(request, *args, **argv):
    return render(request, '404.html')