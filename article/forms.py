from django.forms import ModelForm, ClearableFileInput
from django.utils.translation import gettext_lazy as _

from .models import ArticleSubmission

class ArticleSubmissionForm(ModelForm):
    class Meta:
        model = ArticleSubmission
        exclude = ['user', 'body',]
        field_requireds = {
            'title': _('Title is required.'),
            'email': _('Email is required for validation purpose.'),
            'documents': _('At least 1 document is required.'),
        }
        labels = {
            'as_anonymous': _('Submit Anonymously'),
            'documents': _('Upload Document'),
        }