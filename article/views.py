from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from hitcount.views import HitCountDetailView

from .models import Article, Comment


class ArticleDetailView(HitCountDetailView):
    model = Article
    template_name = 'article/single-standard.html'
    context_object_name = 'article'
    count_hit = True
    
    def get_previous_article(self):
        article_id = self.get_object().id
        if article_id > 1:
            previous_article = Article.objects.get(id=article_id-1)
        else:
            previous_article = Article.objects.get(id=1)
        
        return previous_article
    
    def get_next_article(self):
        article_id = self.get_object().id
        if article_id < Article.objects.count():
            next_article = Article.objects.get(id=article_id + 1)
        else:
            next_article = Article.objects.get(id=Article.objects.count())
        
        return next_article
    
    
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=self.get_object())
        context['previous_article'] = self.get_previous_article()
        context['next_article'] = self.get_next_article()
        return context
        

class SearchArticlesListView(ListView):
    model = Article
    template_name = 'article/search-articles.html'
    paginate_by = 10
    context_object_name = 'articles'
    
    def get_queryset(self):
        articles = super(SearchArticlesListView, self).get_queryset()
        query = self.kwargs.get('query', None)
        articles = Article.objects.filter(title__contains=query)

        sort_by = self.request.GET.get('sort_by', '')
        date_from = self.request.GET.get('date_from', '')
        date_to = self.request.GET.get('date_to', '')

        if sort_by == 'popular':
            articles = articles.order_by('-hit_count_generic__hits')
        elif sort_by == 'newest':
            articles = articles.order_by('-date')
        elif sort_by == 'oldest':
            articles = articles.order_by('date')
        
        if date_from and date_to:
            articles = articles.filter(date__range=(date_from, date_to))
        
        return articles
    
    def get_context_data(self, **kwargs):
        context = super(SearchArticlesListView, self).get_context_data(**kwargs)
        context['query'] = self.kwargs.get('query', None)
        context['filters'] = {
            'sort_by': self.request.GET.get('sort_by', ''),
            'date_from': self.request.GET.get('date_from', ''),
            'date_to': self.request.GET.get('date_to', ''),
        }
        return context


def blog(request):
    return render(request, 'article/article-detail.html')
def blog_detail(request, blog):
    return render(request, 'article/article-detail.html')