from django.urls import path

from . import views

app_name = 'article'
urlpatterns = [
    path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='detail'),
    path('submit/', views.ArticleSubmissionView.as_view(), name='submit'),
    path('submit/success/', views.article_submission_success, name='submit-success'),
    path('search/<str:query>/', views.SearchArticlesListView.as_view(), name='search'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<slug:blog>/', views.blog_detail, name='blog_detail'),
]
