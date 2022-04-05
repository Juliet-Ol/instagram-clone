
from django.test import TestCase
from .models import Image, Profile, Post, Comment

# Set up method 
class ImageTestClass(TestCase):
    def setUp(self):
        self.breakfast=Image(image='image', image_name='breakfast', image_caption='Important',)

    def test_instance(self):
        self.assertTrue(isinstance(self.breakfast,Image))

#Testing Save Method

    def test_save_method(self):
        self.breakfast.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>1)

#Tesing Delete Method
    def test_delete_method(self):
        self.breakfast.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>1)   


# Set up method 
class ProfileTestClass(TestCase):
    def setUp(self):
        self.juliet=Profile(avatar='avatar', author='juliet', name='juliet', bio='juliet')

    def test_instance(self):
        self.assertTrue(isinstance(self.juliet, Profile))


#Testing Save Method

    def test_save_method(self):
        self.juliet.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>1)

#Tesing Delete Method
    def test_delete_method(self):
        self.juliet.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>1) 



# Set up method        


class PostTestClass(TestCase):
    def setUp(self):
        self.breakfast=Post(title='breakfast', post='hey', author='juliet', published_date='Aprill4', picture='picture')

    def test_instance(self):
        self.assertTrue(isinstance(self.breakfast, Post))  


#Testing Save Method

    def test_save_method(self):
        self.breakfast.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts)>1)

#Tesing Delete Method
    def test_delete_method(self):
        self.breakfast.delete_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts)>1)

# Set up method        


class CommentTestClass(TestCase):
    def setUp(self):
        self.juliet=Comment(post='', author='juliet', comment='good', created_on='Aprill4')

    def test_instance(self):
        self.assertTrue(isinstance(self.juliet, Comment))  


    #Testing Save Method

    def test_save_method(self):
        self.juliet.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)>1)

#Tesing Delete Method
    def test_delete_method(self):
        self.juliet.delete_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)>1)            





        


