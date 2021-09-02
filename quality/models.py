from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Location(models.Model):
    area = models.CharField(max_length=20)

    def __str__(self):
        return self.area

class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=20)
    image_description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    location = models.ManyToManyField(Location)
    posted = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)