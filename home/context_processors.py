from article.models import Category

def categories(request):
    return {'categories': Category.objects.all()[::-1]}