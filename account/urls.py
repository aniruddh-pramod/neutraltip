from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('<str:user>/', views.user_profile, name='user_profile'),
    path('<str:user>/edit', views.UserProfileEditView.as_view(), name='user_profile_edit'),
]
