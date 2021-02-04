from django.db import models

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=99)
    author = models.CharField(max_length=20)
    slug = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(blank=True)
    content = models.TextField()

    def __str__(self):
        return f" {self.title} --->>> ({self.author})"

