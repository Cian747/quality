from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20,null=False,blank=False)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id,name):
        return cls.objects.filter(id = id).update(name=name)


    @classmethod
    def all_categories(cls):
        categories = cls.objects.all()
        return categories

    def __str__(self):
        return self.name

class Location(models.Model):
    area = models.CharField(max_length=20)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, id,area):
        return cls.objects.filter(id = id).update(area=area)

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

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id = id)
        return image

    @classmethod
    def update_image(cls, id,image):
        return cls.objects.filter(id = id).update(image=image)

    @classmethod
    def filter_by_location(cls,location):
        return cls.objects.filter(location__area__icontains = location).all()
       

    @classmethod
    def search_category(cls,search_category):
        return cls.objects.filter(category__name__icontains = search_category).all()
    
    @classmethod
    def image_location(cls,location):
        see_location = cls.objects.filter(location__area__icontains = location).all()
        return see_location

    @classmethod
    def copy_image(cls,id,image):
        return cls.objects.filter(id = id).copy(image=image)
        


# Create update methods and copy link method