from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.contrib.auth import logout

from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required

from .models import UserProfile
from article.models import Article
from .forms import UserProfileEditForm

# Create your views here.

def user_profile(request, user):
    user = get_object_or_404(User, username=user)
    if not user.userprofile.display_profile:
        return HttpResponse(status=404)

    tab = request.GET.get('tab')

    context = {
        'tab': tab,
        'user': user,
        'can_edit': user == request.user,
    }

    if tab == 'articles':
        articles = Article.objects.filter(author=user)
        context['articles'] = articles
    return render(request, 'account/user-profile.html', context)


class UserProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileEditForm
    template_name = 'account/user-profile-edit.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        if self.request.user.is_authenticated:
            obj = UserProfile.objects.get(user=self.request.user)
            return obj
        else:
            raise Http404('u trynna be funny?')
    
    def get_success_url(self):
        return self.get_redirect_url(self.request.user)
    
    def get_redirect_url(self, user):
        return reverse_lazy('account:user_profile_edit',
                            current_app='account')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))