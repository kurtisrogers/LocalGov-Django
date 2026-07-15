"""Admin registrations for news."""

from django.contrib import admin

from news.models import NewsArticle, Newsroom


class NewsArticleInline(admin.TabularInline):
    model = NewsArticle
    extra = 0
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Newsroom)
class NewsroomAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [NewsArticleInline]


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "newsroom", "published_date", "featured", "published"]
    list_filter = ["newsroom", "featured", "published"]
