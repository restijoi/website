from django.db import models
from django.contrib.auth.models import User
from updown.fields import RatingField
from tagging.registry import register

class Project(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    problem = models.CharField(max_length=255, null=True, blank=True)
    rating = RatingField(can_change_vote=True)
    image = models.ImageField(upload_to="images")
    public_views = models.IntegerField(default=0)
    private_views = models.IntegerField(default=0)
    funding = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    goal = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    paypal =models.EmailField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.name;

register(Project)

class Team(models.Model):
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)
    role = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.project;


class Group(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name;


class Benefit(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name;


class Barrier(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name;


class Collaborator(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name;

#class Grants(models.Model):

# grant progress...

#class Service(models.Model):
#    name = models.CharField(max_length=200)
#    slug = models.SlugField(max_length=200, unique=True)


