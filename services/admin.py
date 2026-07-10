"""Admin registrations for services."""

from django.contrib import admin

from services.models import ServiceLandingPage, ServicePage, ServiceStatus, ServiceSubLandingPage


class ServiceSubLandingInline(admin.TabularInline):
    model = ServiceSubLandingPage
    extra = 0
    prepopulated_fields = {"slug": ("title",)}


class ServicePageInline(admin.TabularInline):
    model = ServicePage
    extra = 0
    prepopulated_fields = {"slug": ("title",)}


class ServiceStatusInline(admin.TabularInline):
    model = ServiceStatus
    extra = 0
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ServiceLandingPage)
class ServiceLandingPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "published", "modified"]
    list_filter = ["published"]
    search_fields = ["title"]
    inlines = [ServiceSubLandingInline, ServicePageInline, ServiceStatusInline]


@admin.register(ServiceSubLandingPage)
class ServiceSubLandingPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "service", "order", "published"]
    list_filter = ["service", "published"]


@admin.register(ServicePage)
class ServicePageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "service", "published"]
    list_filter = ["service", "published"]


@admin.register(ServiceStatus)
class ServiceStatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "service", "severity", "active", "published"]
    list_filter = ["service", "severity", "active", "published"]
