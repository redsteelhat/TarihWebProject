# models.py

from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import truncatechars  # Önizleme metnini kesmek için



class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()  # CKEditor ile zengin metin alanı


    def __str__(self):
        return self.title

    def short_preview(self):
        return truncatechars(self.content, 200)  # İlk 200 karakterlik kısmı al

class BlogImage(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blog_images/')
