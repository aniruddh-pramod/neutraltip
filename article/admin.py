from django.contrib import admin

from .models import Article, Comment, Tag, Category, ArticleSubmission

# Register your models here.

class CommentAdmin(admin.TabularInline):
    model = Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date', 'time', 'updated_at', 'views')
    list_filter = ('category', 'date', 'updated_at')
    search_fields = ('title', 'body', 'excerpt',)
    inlines = [CommentAdmin]

    def views(self, obj):
        return obj.hit_count.hits

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'article', 'datetime')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(ArticleSubmission)
class ArticleSubmissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'datetime', 'status')
    list_filter = ('status', 'datetime')
    search_fields = ('title', 'body', 'summary',)   