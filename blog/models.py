from django.db import models
from django.urls import reverse
# Create your models here.

class Newsletter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

class Carousel(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='carousel/')


    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='about/')
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        return reverse("aboutDetailView", args=[self.slug])

    def __str__(self):
        return self.name

class Features(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='features/')

    def __str__(self):
        return self.name

class Pricing(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pricing/')

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='testimonial/')


    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='blog/')


    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    data = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.TextField()
    massage = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    subject = models.TextField()

    def __str__(self):
        return self.name


