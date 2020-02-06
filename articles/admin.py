from django.contrib import admin
from .models import Article, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    # help we can see comment on article in admin site.
    inlines = [
        CommentInLine,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
