from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('family/<int:family_id>', views.family_detail, name='family_detail'),
    path('animal/<int:animal_id>', views.animal_detail, name='animal_detail'),
]
