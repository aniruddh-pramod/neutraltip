from django.forms import ModelForm

from .models import UserProfile

class UserProfileEditForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
    