from django.shortcuts import render

# Create your views here.

class Animal(object):
    def __init__(self, id, legs, weight):
        self.id = id
        self.legs = legs
        self.weight = weight
        def __str__(self):
            return "Animal #%s, %s legs, %s kg" % (self.id, self.legs, self.weight)
        
class Animal(object):
    def __init__(self, id, height, speed, family):
        self.id = id
        self.height = height
        self.speed = speed
        self.family = family
        def __str__(self):
            return "Animal #%s, %s cm, %s m/s, family %s" % (self.id, self.height, self.speed, self.family)
        
class Family(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        def __str__(self):
            return "Family %s, %s" % (self.id, self.name)
        






