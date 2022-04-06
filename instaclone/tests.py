
from django.test import TestCase
from .models import Image, Profile, Post, Comment

# Set up method 
class ImageTestClass(TestCase):
    def setUp(self):
        self.image=Image(image_name='breakfast')

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

#Testing Save Method

    def test_save_method(self):
        self.breakfast.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

 


# Set up method 
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile=Profile(name='juliet')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))





# # Set up method        


class PostTestClass(TestCase):
    def setUp(self):
        self.breakfast=Post(title='breakfast', post='hey', published_date='Aprill4', picture='picture')

    def test_instance(self):
        self.assertTrue(isinstance(self.breakfast, Post))  



# # Set up method        


class CommentTestClass(TestCase):
    def setUp(self):
        self.good=Comment(comment='good', created_on='Aprill4')

    def test_instance(self):
        self.assertTrue(isinstance(self.good, Comment))  


        





        


