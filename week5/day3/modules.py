from django.db import models

class Gif(models.Model):

    title = models.CharField(max_length=50)
    url = models.URLField()
    uploader_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}, {self.uploader_name}'
    
class Category(models.Model):

    name = models.CharField(max_length=50)
    gifs = models.ManyToManyField(Gif, related_name='categories')

    def __str__(self) -> str:
        return f'{self.name}'