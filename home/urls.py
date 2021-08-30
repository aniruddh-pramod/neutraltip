from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('support/', views.support, name='support'),
    path('credits/', views.credits, name='credits'),
    path('faq/', views.faq, name='faq'),
]
