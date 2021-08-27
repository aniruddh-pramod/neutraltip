from django.urls import path

from .views import ArticleListView

urlpatterns = [
    path('<str:slug>/', ArticleListView.as_view(), name='article-detail'),
]
