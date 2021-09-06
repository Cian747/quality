from django.test import TestCase
from .models import Category,Images,Location
import  datetime as dt
from django.contrib.auth.models import User
# Create your tests here.

class ImagesTestClass(TestCase):

    def setUp(self):
        '''
        Create set up of all classes
        '''
        self.new_user = User(id = 1,first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.new_user.save()

        self.category = Category(id = 1,name = 'yoko')
        self.category.save()
        
        self.location = Location(id = 1,area = 'Japan')
        self.location.save()

        self.new_images = Images(id = 1,image='image.jpg',image_name ='serene' ,image_description='The alps' ,user= self.new_user ,location = self.location,posted = '1980-06-04')
        self.new_images.save_image()


    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Images.objects.all().delete()

    # Test if set up matches the class
    def test_image_instance(self):
        self.assertTrue(isinstance(self.new_images,Images))

    def test_location_instance(self):
        self.assertTrue(isinstance(self.location,Location))
    
    def test_category_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def test_fetch_by_image_id(self):
        '''
        Fetch an image by it's id
        '''
        found_image = self.new_images.get_image_by_id(self.new_images.id)
        self.assertTrue(len(found_image)>0)

    # Test save categories
    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)== 1)
    
    def test_save_location(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location)== 1)
    
    def test_save_image(self):
        self.new_images.save_image()
        new_images = Images.objects.all()
        self.assertTrue(len(new_images) == 1)

    # Test fetch all classes
    def test_fetch_all(self):
        '''
        Test if you can fetch all images
        '''
        all_images = Images.fetch_all()
        self.assertTrue(len(all_images)>0)

    def test_all_categories(self):
        '''
        Test if you can fetch all categories
        '''
        all_categories = Category.all_categories()
        self.assertTrue(len(all_categories)>0)

    def test_fetch_all_locations(self):
        '''
        Test to to fetch all saved locations from db
        '''
        all_locations = Location.all_locations()
        self.assertTrue(len(all_locations)>0)

    # Test delete in classes  
    def test_delete_images(self):
        '''
        test if you can delete images
        '''
        self.new_images.delete_image()
        new_images = Images.objects.all()
        self.assertTrue(len(new_images)==0)


    def test_delete_location(self):
        '''
        Test if you can delete location
        '''
        self.location.delete_location()
        all_locations = Location.all_locations()
        self.assertTrue(len(all_locations)==0)

    def test_delete_category(self):
        '''
        Test if you can delete category
        '''
        self.category.delete_category()
        all_categories = Category.objects.all()
        self.assertTrue(len(all_categories) == 0)

    # Test for search functionality
    def test_search_location(self):
        '''
        Test if you can search for location
        '''
        images = Images.filter_by_location('Japan')
        self.assertTrue(len(images) == 1)
    
    # def test_search_category(self):
    #     '''
    #     Search by category
    #     '''
    #     images = Images.search_category('Amber')
    #     self.assertTrue(len(images)>0)

    
    # Test updates
    def test_update_location(self):
        '''
        Test to update location
        '''
        self.location.save()
        location  = Location.objects.last().id
        Location.update_location(location,'Zanzibar')
        update_location = Location.objects.get(id = location)
        self.assertEqual(update_location.area,'Zanzibar')
        
    def test_update_category(self):
        '''
        Update category class
        '''
        self.category.save()
        category  = Category.objects.last().id
        Category.update_category(category,'English')
        update_category = Category.objects.get(id = category)
        self.assertEqual(update_category.name,'English')
    
    def test_update_images(self):
        '''
        Update image class
        '''
        self.new_images.save()
        image = Images.objects.last().id
        Images.update_image(image,'cat.jpg')
        update_image = Images.objects.get(id = image)
        self.assertEqual(update_image.image,'cat.jpg') 

    


        

