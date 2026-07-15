"""Admin registrations for alerts."""

from django.contrib import admin

from alerts.models import AlertBanner


@admin.register(AlertBanner)
class AlertBannerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "alert_type", "active", "published"]
    list_filter = ["alert_type", "active", "published"]
