from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    slug = models.CharField(max_length=500, unique=True)
    def __str__(self):
        return self.name
class Slider(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    url = models.URLField(max_length=500,blank = True)
    def __str__(self):
        return self.title
class Ad(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    url = models.URLField(max_length=500,blank = True)
    rank = models.IntegerField()
    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=500, unique=True)
    def __str__(self):
        return self.title
