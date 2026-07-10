"""Admin registrations for step by step."""

from django.contrib import admin

from step_by_step.models import StepByStepOverview, StepByStepPage


class StepByStepPageInline(admin.TabularInline):
    model = StepByStepPage
    extra = 0
    prepopulated_fields = {"slug": ("title",)}


@admin.register(StepByStepOverview)
class StepByStepOverviewAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [StepByStepPageInline]


@admin.register(StepByStepPage)
class StepByStepPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "overview", "step_number", "published"]
