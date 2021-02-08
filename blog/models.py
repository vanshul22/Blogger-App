from django.db import models

# Create your models here.

class Post(models.Model):
    # Created Some Models for Submitting Data into DataBases
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=99)
    author = models.CharField(max_length=20)
    slug = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(blank=True)
    content = models.TextField()

    # Created templates How Blogs Shows in Admin Panel
    def __str__(self):
        return f" {self.title} --->>> ({self.author})"

