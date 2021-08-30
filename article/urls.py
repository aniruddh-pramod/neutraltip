from django.urls import path

from . import views

app_name = 'article'
urlpatterns = [
    path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='detail'),
    path('search/<str:query>/', views.SearchArticlesListView.as_view(), name='search'),
    path('category/', views.category_list, name='category_list'),
    path('category/<str:category>/', views.category, name='category_page'),
    path('tag/<str:tag>/', views.tag, name='tag_page'),
    path('blog/', views.blog, name='blog_index'),
    path('blog/<slug:blog>/', views.blog_detail, name='blog_detail'),
]
