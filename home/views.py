from django.shortcuts import render

from article.models import Article, Tag

# Create your views here.

def index(request):
    # Selecting articles with featured tag
    featured_tag = Tag.objects.get(name='featured')
    featured_articles = Article.objects.filter(tags=featured_tag)[:3]

    articles = Article.objects.all()[:12]
    context = {
        'featured_articles': featured_articles,
        'articles': articles,
    }
    return render(request, 'home/index.html', context)