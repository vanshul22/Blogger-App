from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bloghome(request):
    """
    docstring
    """
    # return HttpResponse("This is a blog home")
    return render(request, "blog/index.html")


def blogpost(request, slug):
    """
    docstring
    """
    # return HttpResponse(f"This is blog post : {slug} ")
    return render(request, "blog/blogpost.html", {"slug":slug})