"""Admin registrations for guides."""

from django.contrib import admin

from guides.models import GuideOverview, GuidePage


class GuidePageInline(admin.TabularInline):
    model = GuidePage
    extra = 0
    prepopulated_fields = {"slug": ("title",)}


@admin.register(GuideOverview)
class GuideOverviewAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [GuidePageInline]


@admin.register(GuidePage)
class GuidePageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "guide", "order", "published"]
