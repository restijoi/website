from django.db import models
from django.contrib.auth.models import User
from updown.fields import RatingField

class Project(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    rating = RatingField(can_change_vote=True)
    image = models.ImageField(upload_to="images")
    public_views = models.IntegerField(default=0)
    private_views = models.IntegerField(default=0)
    funding = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    goal = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    paypal =models.EmailField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)