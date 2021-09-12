from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin

from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from django.urls import reverse

from datetime import datetime
import os, uuid

from .validators import validate_file_size

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Tag, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Tags'



class Article(models.Model, HitCountMixin):
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    tags = models.ManyToManyField(Tag, blank=False, related_name='tag')
    slug = models.SlugField(default='', editable=False, max_length=200, null=False, unique=True)
    body = models.TextField()
    excerpt = models.TextField(max_length=500, blank=True)
    show_excerpt_in_article = models.BooleanField(default=True)
    date = models.DateField(default=datetime.now)
    time = models.TimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    thumb = models.ImageField(blank=True, upload_to='article/article_thumbs')
    thumb_alt = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
    
    def get_datetime(self):
        return datetime.combine(self.date, self.time)

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('article-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title + '--' +
                                get_random_string(length=7))
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date']



class Comment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-datetime']


# article request submition model
class ArticleSubmission(models.Model):
    # converting filename into random string
    def get_hashed_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('article/submissions/documents/', filename)
    
    status_choices = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    as_anonymous = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField(blank=True)
    summary = models.TextField(max_length=500, blank=True)
    additional_info = models.TextField(max_length=500, blank=True)
    thumb = models.ImageField(upload_to='article/submissions/submission_thumbs', blank=True)
    thumb_alt = models.CharField(max_length=50, default='', blank=True)
    datetime = models.DateTimeField(auto_now=True)
    documents = models.FileField(upload_to=get_hashed_file_path, validators=[validate_file_size], blank=False)
    status = models.CharField(choices=status_choices, max_length=50, default='pending')
    
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.documents:
            self.documents.delete()
            super().delete(*args, **kwargs)

    class Meta:
        ordering = ['-datetime']