from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bloghome(request):
    """
    docstring
    """
    return HttpResponse("This is a blog home")


def blogpost(request, slug):
    """
    docstring
    """
    return HttpResponse(f"This is blog post : {slug} ")