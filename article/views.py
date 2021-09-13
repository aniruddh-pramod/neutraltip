from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from hitcount.views import HitCountDetailView
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from .forms import ArticleSubmissionForm
from .models import Article, Comment, ArticleSubmission


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
        articles = Article.objects.filter(title__icontains=query)

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

class ArticleSubmissionView(SuccessMessageMixin, CreateView):
    model = ArticleSubmission
    form_class = ArticleSubmissionForm
    template_name = 'article/submit-article.html'
    context_object_name = 'article'
    success_url = reverse_lazy('article:submit-success')
    success_message = 'Your article request has been submitted successfully. Expect a response within 48 hrs.'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid() and request.user.is_authenticated:
            form.instance.user = User.objects.get(username=request.user)
            form.instance.save()
            return self.form_valid(form)
        else:
            return self.form_valid(form)


class BlogView(ListView):
    model = Article
    template_name = 'article/blog.html'
    context_object_name = 'articles'

    def get_queryset(self):
        articles = super(BlogView, self).get_queryset()
        articles = articles.filter(tags__name='blog').order_by('-date')
        return articles

def article_submission_success(request):
    return render(request, 'article/submit-success.html')

def blog(request):
    return render(request, 'article/blog.html')
def blog_detail(request, blog):
    return render(request, 'article/blog-post.html')