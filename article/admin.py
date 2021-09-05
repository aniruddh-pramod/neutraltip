from django.contrib import admin

from .models import Article, Comment, Tag, Category, ArticleSubmission

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date', 'time', 'updated_at', 'views')
    list_filter = ('category', 'date', 'updated_at')
    search_fields = ('title', 'body', 'excerpt',)

    def views(self, obj):
        return obj.hit_count.hits

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'article', 'datetime')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(ArticleSubmission)
class ArticleSubmissionAdmin(admin.ModelAdmin):
    pass