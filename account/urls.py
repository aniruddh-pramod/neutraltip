from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('<str:user>/', views.user_profile, name='user_profile'),
]
