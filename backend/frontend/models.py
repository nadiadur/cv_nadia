from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return self.name
