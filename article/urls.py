from django.urls import path

from . import views

urlpatterns = [
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('category/', views.category_list, name='category_list'),
    path('category/<str:category>/', views.category, name='category_page'),
    path('blog/', views.blog, name='blog_index'),
    path('blog/<slug:blog>/', views.blog_detail, name='blog_detail'),
    path('about/', views.about, name='about_page'),
    path('contact/', views.contact, name='contact_page'),
]
