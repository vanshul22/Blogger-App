from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.

# Handling Blog Homes Here
def bloghome(request):
    """
    docstring
    """
    # fetching data from database.
    allposts = Post.objects.all()
    # sending data to front end.
    context = {'allposts' : allposts, }
    # return HttpResponse("This is a blog home")
    return render(request, "blog/index.html", context)

# Handling Blog Post Here
def blogpost(request, slug):
    """
    docstring
    """
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    # return HttpResponse(f"This is blog post : {slug} ")
    return render(request, "blog/blogpost.html", context)