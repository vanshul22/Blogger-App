from django.db import models

# Create your models here.

class Contact(models.Model):
    # Created Models for takig value of contact.html
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=30)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        """
        Showing This string in Admin Panel. For displaying Contact object.
        """
        return f"Message from {self.name}, ({self.email})"
