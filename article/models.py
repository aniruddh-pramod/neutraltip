from django.db import models
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from django.urls import reverse


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default='', editable=False, max_length=200, null = False, unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    auto_now_add = True
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
    
    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('article-detail', kwargs=kwargs)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title + '--' + get_random_string(length=7))
        super(Article, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date']


class Tag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Tags'

class Category(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'