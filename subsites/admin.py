"""Admin registrations for subsites."""

from django.contrib import admin

from subsites.models import SubsiteOverview, SubsitePage


class SubsitePageInline(admin.TabularInline):
    model = SubsitePage
    extra = 0
    prepopulated_fields = {"slug": ("title",)}


@admin.register(SubsiteOverview)
class SubsiteOverviewAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [SubsitePageInline]


@admin.register(SubsitePage)
class SubsitePageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "subsite", "published"]
