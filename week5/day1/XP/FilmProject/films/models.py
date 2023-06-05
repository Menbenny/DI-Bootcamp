from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Film(models.Model):
    tittle = models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True)
    created_in_country = models.ForeignKey(Country, 
                                           on_delete=models.CASCADE,
                                           related_name='films_created')
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)