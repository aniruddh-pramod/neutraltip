from django import template
from django.utils.safestring import mark_safe

from django.urls import reverse
from datetime import datetime

register = template.Library()


@register.simple_tag
def profile_pic(user):
    profile = user.userprofile

    if user.is_authenticated == False or not profile.display_profile:
        return ''
    
    if profile.dob:
        profile_dob = profile.dob.strftime('%d/%m/%Y')
    else:
        profile_dob = ''

    if profile.profile_pic:
        return mark_safe(f'<img class="profile-pic" src="{profile.profile_pic.url}" alt="{profile.get_full_name()}" />')
    else:
        return mark_safe(f'<svg data-jdenticon-value="{user}"></svg>')


@register.simple_tag
def user_name(user, href=False):
    if user.is_authenticated == False or not user.userprofile.display_profile:
        return ''

    profile = user.userprofile
    
    if profile.get_full_name:
        if href:
            return mark_safe(f'<a href="{reverse("account:user_profile", kwargs={"user": user.username})}">{profile.get_full_name()}</a>')
        else:
            return mark_safe(f'{profile.get_full_name()}')
    else:
        if href:
            return mark_safe(f'<a href="{reverse("account:user_profile", kwargs={"user": user.username})}">{user.username}</a>')
        else:
            return mark_safe(f'{user.username}')