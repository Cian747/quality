from django.test import TestCase
from .models import Category,Images,Location
import  datetime as dt
from django.contrib.auth.models import User
# Create your tests here.

class ImagesTestClass(TestCase):

    def setUp(self):
        self.new_user = User(id = 1,first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.new_user.save()

        self.category = Category(id = 1,name = 'yoko')
        self.category.save()
        
        self.location = Location(id = 1,area = 'Japan')
        self.location.save()

        self.new_images = Images(id = 1,image='image.jpg',image_name ='serene' ,image_description='The alps' ,user= self.new_user ,posted = '1980-06-04')
        self.new_images.save()


    def tearDown(self):
        Category.objects.all().delete()
        Images.objects.all().delete()
        Location.objects.all().delete()

    def test_image_instance(self):
        self.assertTrue(isinstance(self.new_images,Images))

    def test_location_instance(self):
        self.assertTrue(isinstance(self.location,Location))
    
    def test_category_instance(self):
        self.assertTrue(isinstance(self.category,Category))
    
    def test_fetch_all(self):
        all_images = Images.fetch_all()
        self.assertTrue(len(all_images)>0)

    # def test_delete_images(self):
    #     self.new_images = Images.delete_image()
    #     self.assertTrue(len(self.new_images)==0)

    def test_fetch_by_image_id(self):
        found_image = Images.fetch_all()
        found_image = Images.get_image_by_id(1)
        self.assertTrue(len(found_image)==1)

    # def test_search_location(self,location):
    #     images = Images.search_by_location(location)
    #     self.assertTrue(len(images)>0)

    # def test_search_category(self):
    #     images = Images.search_category(self.category)
    #     self.assertTrue(len(images)>0)SS


        

