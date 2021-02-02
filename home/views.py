from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact

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
    if request.method == "POST":
        name = request.POST['name'],
        email = request.POST['email'],
        phone = request.POST['phone'],
        content = request.POST['content']
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()

    # return HttpResponse("This is contact of home")
    return render(request, "home/contact.html")
