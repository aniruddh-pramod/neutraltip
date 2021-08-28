from django.http import HttpResponse
from django.shortcuts import render

from .models import Article

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    article_id = article.id

    # Previous article
    if article_id > 1:
        previous_article = Article.objects.get(id=article_id - 1)
    else:
        previous_article = Article.objects.get(id=1)
    
    # Next article
    if article_id < Article.objects.count():
        next_article = Article.objects.get(id=article_id + 1)
    else:
        next_article = Article.objects.get(id=Article.objects.count())

    context = {
        'article': article,
        'previous_article': previous_article,
        'next_article': next_article,
    }
    return render(request, 'article/single-standard.html', context)


def blog(request):
    return render(request, 'article/article-detail.html')
def blog_detail(request, blog):
    return render(request, 'article/article-detail.html')
def category(request, category):
    return render(request, 'article/article-detail.html')
def category_list(request):
    return render(request, 'article/article-detail.html')
def tag(request, tag):
    return render(request, 'article/article-detail.html')
def about(request):
    return render(request, 'article/article-detail.html')
def contact(request):
    return render(request, 'article/article-detail.html')