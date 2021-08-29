from django.shortcuts import render

from article.models import Article, Tag

import math

# Create your views here.

def validate_page_number(number, paginations):
    # if number is positive integer
    number = int(number) if (number.isdigit() and int(number) > 0) else 1
    # if number is in pagination range
    number = number if number <= paginations else paginations
    
    return number


def index(request):
    # Selecting articles with featured tag
    featured_tag = Tag.objects.get(name='featured')
    featured_articles = Article.objects.filter(tags=featured_tag)[:3]

    # Pagination
    paginations = math.ceil(Article.objects.all().count() / 2)

    page_no = request.GET.get('page', '1')
    page_no = validate_page_number(page_no, paginations)

    pagination_start = (page_no - 1) * 2
    pagination_end = pagination_start + 2

    relative_paginations = paginations + (page_no - 1) if paginations > 9 else paginations

    articles = Article.objects.all()[pagination_start:pagination_end]

    context = {
        'featured_articles': featured_articles,
        'articles': articles,
        'paginations': range(1, relative_paginations + 1),
        'current_page': page_no,
    }
    return render(request, 'home/index.html', context)