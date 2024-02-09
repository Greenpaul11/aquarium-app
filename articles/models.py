from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    bold_text = models.CharField(max_length=50, blank=True)
    text_part = models.TextField(blank=True)
    main_photo = models.ImageField(upload_to='static/article_photos')
    created = models.DateTimeField(auto_now_add=True)
    

class Photo(models.Model):
    description = models.CharField(max_length=50)
    article = models.ManyToManyField(Article, related_name='image')
    image = models.ImageField(upload_to='static/article_photos') 
    

class Tag(models.Model):
    tag_text =  models.CharField(max_length=50)
    article = models.ManyToManyField(Article, related_name='article_tag')
    

class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment
