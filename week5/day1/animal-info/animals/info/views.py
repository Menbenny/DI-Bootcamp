from django.shortcuts import render
from .models import Family, Animal

def family_detail(request, family_id):
    family = get_object_or_404(Family, id=family_id)
    animals = family.animal_set.all()
    return render(request, 'family_detail.html', {'family': family, 'animals': animals})

def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'animal_detail.html', {'animal': animal})