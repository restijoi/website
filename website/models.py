from django.db import models
from django.contrib.auth.models import User
from updown.fields import RatingField


# Create your models here.
#project 
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class Project(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    rating = RatingField(can_change_vote=True)
    image = models.ImageField(upload_to="images")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)