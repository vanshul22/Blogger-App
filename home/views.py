from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """
    docstring
    """
    return HttpResponse("this is home of home")


def about(request):
    """
    docstring
    """
    return HttpResponse("This is about of home")


def contact(request):
    """
    docstring
    """
    return HttpResponse("This is contact of home")