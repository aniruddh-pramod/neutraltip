from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required

from article.models import Article

# Create your views here.

def user_profile(request, user):
    user = get_object_or_404(User, username=user)
    if not user.userprofile.display_profile:
        return HttpResponse(status=404)

    tab = request.GET.get('tab')

    context = {
        'tab': tab,
        'user': user,
    }

    if tab == 'articles':
        articles = Article.objects.filter(author=user)
        context['articles'] = articles
    return render(request, 'account/user-profile.html', context)