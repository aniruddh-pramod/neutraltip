from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from home.models import Faq
from article.models import Article, Tag, Category

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

class CategoryListView(ListView):
    model = Article
    template_name = 'home/category.html'
    context_object_name = 'articles'
    paginate_by = 12

    def get_queryset(self):
        # Call the base implementation first to get a context
        articles = super(CategoryListView, self).get_queryset()
        # Add extras
        category_id = Category.objects.get(name=self.kwargs['category']).id
        articles = articles.filter(category=category_id)[:108]
        return articles

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CategoryListView, self).get_context_data(**kwargs)
        # Add extras
        context['category'] = self.kwargs['category']

        return context

class TagListView(ListView):
    model = Article
    template_name = 'home/tag.html'
    context_object_name = 'articles'
    paginate_by = 12

    def get_queryset(self):
        # Call the base implementation first to get a context
        articles = super(TagListView, self).get_queryset()
        # Add extras
        tag = self.kwargs['tag']
        articles = articles.filter(tags__name__in=[tag])[:108]
        return articles

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TagListView, self).get_context_data(**kwargs)
        # Add extras
        context['tag'] = self.kwargs['tag']
        return context


class FaqListView(ListView):
    model = Faq
    template_name = 'home/faq.html'
    context_object_name = 'faqs'
    paginate_by = 7

def category_all(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'home/category_all.html', context)