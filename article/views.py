from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Article

class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'article/article.html'
class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article/article_post.html'
