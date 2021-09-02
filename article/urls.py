from django.urls import path

from . import views

app_name = 'article'
urlpatterns = [
    path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='detail'),
    path('search/<str:query>/', views.SearchArticlesListView.as_view(), name='search'),
    path('blog/', views.blog, name='blog_index'),
    path('blog/<slug:blog>/', views.blog_detail, name='blog_detail'),
]
