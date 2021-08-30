from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from article.models import Article, Tag

import math

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'home/index.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        # Call the base implementation first to get a context
        articles = super(ArticleListView, self).get_queryset()
        # Add extras
        articles = articles[:108]
        return articles

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ArticleListView, self).get_context_data(**kwargs)
        # Add extras
        context['featured_articles'] = Article.objects.filter(tags__name__in=['featured'])[:3]

        return context


def about(request):
    return HttpResponse('about')
def contact(request):
    return HttpResponse('contact')
def support(request):
    return HttpResponse('support')
def credits(request):
    return HttpResponse('credits')
def faq(request):
    return HttpResponse('faq')