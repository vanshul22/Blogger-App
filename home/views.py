from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """
    docstring
    """
    # return HttpResponse("this is home of home")
    return render(request, "home/index.html")


def about(request):
    """
    docstring
    """
    # return HttpResponse("This is about of home")
    return render(request, "home/about.html")



def contact(request):
    """
    docstring
    """
    # return HttpResponse("This is contact of home")
    return render(request, "home/contact.html")
