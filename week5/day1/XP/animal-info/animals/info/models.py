from django.db import models

# Create your models here.

from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=50)
    legs = models.PositiveIntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
