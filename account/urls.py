from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('sign-up/', views.sign_up, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('edit/', views.UserProfileEditView.as_view(), name='user_profile_edit'),
    path('<str:user>/', views.user_profile, name='user_profile'),
]
