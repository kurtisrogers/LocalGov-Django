"""Admin registrations for core models."""

from django.contrib import admin

from core.models import MenuItem, SiteConfiguration, Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ["site_name", "council_name"]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["label", "menu_type", "order", "url"]
    list_filter = ["menu_type"]
