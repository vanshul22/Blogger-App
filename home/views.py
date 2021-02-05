from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Contact
# Importing django message module
from django.contrib import messages
# Taking all post from this Post 
from blog.models import Post
# Taking User to create User
from django.contrib.auth.models import User

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


def handlesignup(request):
    if request.method == "POST":
        pass
        # Getting the Post Method
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Checking For Error Inputs

        # Creating User
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Blogger Account Has Been SuccessFully Created")
        return redirect("home")



    else:
        HttpResponse("404 Not Found")