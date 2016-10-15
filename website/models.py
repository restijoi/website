from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#project 
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class Project(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)