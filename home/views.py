from django.shortcuts import render

from article.models import Article

# Create your views here.

def index(request):
    featured_articles = Article.objects.filter(tag='featured')
    articles = Article.objects.all()
    return render(request, 'home/index.html')