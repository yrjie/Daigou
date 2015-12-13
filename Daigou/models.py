from django.db import models
from django.contrib.auth.models import User
from utils import pkgen

class Note(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

class Product(models.Model):
    key = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=511)
    description = models.CharField(max_length=2047)
    owner = models.ForeignKey(UserProfile)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.key = pkgen(type(self))
        super(Product, self).save(*args, **kwargs)
