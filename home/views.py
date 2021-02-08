from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Contact
# Importing django message module
from django.contrib import messages
# Taking all post from this Post 
from blog.models import Post
# Taking User to create User
from django.contrib.auth.models import User
# Authenticate User is verified or not
from django.contrib.auth import authenticate, login, logout


# Create your views here.
""" HTML Pages """
# Handling Home Page Here
def home(request):
    """
    docstring
    """
    # return HttpResponse("this is home of home")
    return render(request, "home/index.html")

# Handle About Page Here
def about(request):
    """
    docstring
    """
    # return HttpResponse("This is about of home")
    return render(request, "home/about.html")

# Handle Contact Page Here
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

# Handle Search Form and Page Here
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
    # return HttpResponse("Search")
    return render(request, "home/search.html", params)

""" Authentication APIs """
# Handle SignUp Here
def handlesignup(request):
    if request.method == "POST":
        # Getting the Post Method
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Checking For Error Inputs
        # Username should be under 10 characters
        if len(username) > 10:
            messages.error(request, "Username Must be Minimum of 10 characters")    
            return redirect("home")

        # Username Should be mixed of Albhabet or Numeric 
        if not username.isalnum():
            messages.error(request, "Username Must be mixed of Alphabet and Numeric") 
            return redirect("home")
            
        # If Passwords does not matching then show error message in home screen
        if password1 != password2:
            messages.error(request, "Password Doesn't Match") 
            return redirect("home")

        # Creating User
        myuser = User.objects.create_user(username, email, password1)
        # Taking User first and last name
        myuser.first_name = fname
        myuser.last_name = lname
        # Saving in data base
        myuser.save()
        # Show user successfull message
        messages.success(request, "Your Blogger Account Has Been SuccessFully Created")
        # Goto home page after login
        return redirect("home")

    else:
        # If anybody comes from URL then show this to user.
        HttpResponse("404 Not Found")

# Handling LOGIN
def handlelogin(request):
    """
    Function For Login Session
    """
    if request.method == "POST":
        # Getting the Post Parametres
        loginusername = request.POST.get("loginusername")
        loginpassword = request.POST.get("loginpassword")
        # Checking user is exist or not for login
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, f"Successfully Logged-IN !!! {loginusername}")
            return redirect("home")
        else:
            messages.error(request, "Check Your Username and Password\n Please try Again...")
            return redirect("home")
    else:
        HttpResponse("404 Not Found")

# Handling LOGOUT
def handlelogout(request):
    """
    Function For LogOut Session
    """
    logout(request)
    messages.success(request, f" Successfully LogOut !!! ")
    return redirect("home")
