from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
# Importing django message module
from django.contrib import messages
# Taking all post from this Post 
from blog.models import Post

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
    Taking Input From Contact.html page and save these fields in their particular variables and also validate form.
    """
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')
        
        # Validation of All Fields
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please Fill the Form Correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your Details Submitted Successfully.")

    # return HttpResponse("This is contact of home")
    return render(request, "home/contact.html")

def search(request):
    """
    Search function it will return search page with matched query.
    """
    query = request.GET["query"]
    if len(query)>50:
        allposts = Post.objects.none()
    else:
        allpostsTitle = Post.objects.filter(title__icontains=query)
        allpostsAuthor = Post.objects.filter(author__icontains=query)
        allpostsContent = Post.objects.filter(content__icontains=query)
        allposts = allpostsTitle.union(allpostsContent, allpostsAuthor)
    if allposts.count()==0:
        messages.warning(request, "No Search Results Found, Please Refine your Query")
    params = {"allposts": allposts, "query":query}
    # return HttpResponse("This is search")
    return render(request, "home/search.html", params)