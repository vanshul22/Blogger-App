from django.contrib import admin

# Register your models here.
from blog.models import Post

# Registering Our Model Here to work with Databases
admin.site.register(Post)