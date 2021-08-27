from django.http import HttpResponse
from django.shortcuts import render

from .models import Article

def article_detail(request, slug):
    context = {
        'article': Article.objects.get(slug=slug)
    }
    return render(request, 'article/article-detail.html', context)


def blog(request):
    return render(request, 'article/article-detail.html')
def blog_detail(request, blog):
    return render(request, 'article/article-detail.html')
def category(request, category):
    return render(request, 'article/article-detail.html')
def category_list(request):
    return render(request, 'article/article-detail.html')
def about(request):
    return render(request, 'article/article-detail.html')
def contact(request):
    return render(request, 'article/article-detail.html')