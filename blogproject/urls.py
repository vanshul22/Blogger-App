"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# To change our Django Administration in Admin Page
admin.site.site_header = "Blogger Administration"
# To change our Django site Admin in Admin login Page or where favicon located.
admin.site.site_title = "Blogger Admin Panel"
# To change our site Administration in Admin Page
admin.site.index_title = "Welcome to Blogger Admin Panel"


urlpatterns = [
    path('admin/', admin.site.urls),
    # Added home app url here if blank is there then goto home app.
    path('', include("home.urls")),
    # Added Blog app here if blog is there then goto blog app.
    path("blog/", include("blog.urls")),
]
