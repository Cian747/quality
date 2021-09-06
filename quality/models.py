from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20,null=False,blank=False)


    @classmethod
    def all_categories(cls):
        categories = cls.objects.all()
        return categories

    def __str__(self):
        return self.name

class Location(models.Model):
    area = models.CharField(max_length=20)

    @classmethod
    def all_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.area

class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=20)
    image_description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=DO_NOTHING)
    posted = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)

    def save_image(self):
        self.save() 

    
    def get_absolute_url(self):
        return reverse('welcome',args=None)

    @classmethod
    def fetch_all(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def delete_image(cls,id):
        del_image = cls.objects.filter(id = id).first()
        return del_image

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id = id).first()
        return image

    @classmethod
    def filter_by_location(cls,location):
        search_location = cls.objects.filter(location__name__icontains = location).all()
        return search_location

    @classmethod
    def search_category(cls,search_category):
        get_category = cls.objects.filter(category__name__icontains = search_category ).all()
        return get_category
    
    @classmethod
    def image_location(cls,location):
        see_location = cls.objects.filter(location__name__icontains = location).all()
        return see_location



