"""Admin registrations for events."""

from django.contrib import admin

from events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "start_date", "location", "published"]
    list_filter = ["published"]
