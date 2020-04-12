from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    '''Model representing a blog post'''
    title = models.CharField(max_length=200)
    post_date = models.DateField(auto_now_add=True, help_text='enter the date')

    #Foreign key is used because blogpost can have only one author(blogger) but bloggers can have multiple blogposts
    #Blogger as a string rather than object becuase it hasn't been declared in the file yet
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    post = models.TextField(max_length=2000, help_text='enter the details here')

    #ManytoManyField used because topic can contain many posts. Posts can cover many topics.
    topic = models.ManyToManyField('Topic', help_text='select topics relevant for this post')

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #Returns the url to access a detailed record of the post
        return reverse('blogpost_detail', args=[str(self.id)])

    def display_topic(self):
        return ', '.join(topic.name for topic in self.topic.all())
    

class Topic(models.Model):
    '''Model represeting a topic'''
    name = models.CharField(max_length=100, help_text='Enter the relevant topic (E.g. Bollywood, Hollywood etc.)')

    def __str__(self):
        return self.name

class Blogger(models.Model):
    '''Model representing an author'''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000, help_text="enter the blogger's bio here")

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


import uuid                         #Required for unique comment instance 

class Comment(models.Model):
    '''Model representing a specific comment'''
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'Unique ID for this particular comment')
    blogpost = models.ForeignKey('BlogPost', on_delete=models.SET_NULL, null=True, related_name='comments')
    post_date = models.DateTimeField(auto_now_add=True, help_text='Please enter date and time')
    comment = models.TextField(max_length=1000)
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.commenter)
    

    
    
