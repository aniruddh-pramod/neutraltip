from django.urls import path

from django.views.generic import TemplateView
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='index'),
    path('category/', views.category_all, name='category_all'),
    path('category/<str:category>/', views.CategoryListView.as_view(), name='category_page'),
    path('tag/<str:tag>/', views.TagListView.as_view(), name='tag_page'),
    path('about/', TemplateView.as_view(template_name='home/about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='home/contact.html'), name='contact'),
    path('support/', TemplateView.as_view(template_name='home/support.html'), name='support'),
    path('credits/', TemplateView.as_view(template_name='home/credits.html'), name='credits'),
    path('faqs/', views.FaqListView.as_view(), name='faqs'),
    path('privacy-policy/', TemplateView.as_view(template_name='home/privacy-policy.html'), name='privacy_policy'),
    path('terms/', TemplateView.as_view(template_name='home/terms.html'), name='terms'),
]
