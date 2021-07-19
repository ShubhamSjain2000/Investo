from django.db import models
from django.contrib.auth.models import User

class Business(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    loction = models.TextField()
    premium = models.BooleanField(default = False)
    img_one = models.ImageField(upload_to='pics/')
    img_two = models.ImageField(upload_to='pics/')
    img_three = models.ImageField(upload_to='pics/')
    address = models.TextField()
    startup = models.BooleanField(default = False)
    shortdescription = models.TextField(default = "No data") 
    
    
    owner = models.CharField(max_length=100)
    opencount = models.IntegerField()
    likes = models.IntegerField()
    
 #   old = models.IntegerField()
#    busstype = models.CharField(max_length=100)
    
    
class Promoters(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    loction = models.TextField()
    businesses = models.TextField()

class Investors(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    loction = models.TextField()
    businesses = models.TextField()

    
    


