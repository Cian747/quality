from django.db import models
import datetime as dt

# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    
class Category(models.Model):
    name = models.CharField(max_length=20)
class Location(models.Model):
    area = models.CharField(max_length=20)

class Images(models.Model):
    image = models.ImageField(upload_to='images')
    image_name = models.CharField(max_length=20)
    image_description = models.TextField()
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    location = models.ManyToManyField(Location)
    posted = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)