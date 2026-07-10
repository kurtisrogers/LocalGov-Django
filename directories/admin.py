"""Admin registrations for directories."""

from django.contrib import admin

from directories.models import (
    DirectoryChannel,
    DirectoryFacet,
    DirectoryFacetType,
    DirectoryOrganisation,
    DirectoryPage,
    DirectoryVenue,
)


@admin.register(DirectoryFacetType)
class DirectoryFacetTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(DirectoryFacet)
class DirectoryFacetAdmin(admin.ModelAdmin):
    list_display = ["name", "facet_type"]
    list_filter = ["facet_type"]


@admin.register(DirectoryChannel)
class DirectoryChannelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "published"]
    filter_horizontal = ["facets", "topics"]


@admin.register(DirectoryPage)
class DirectoryPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "primary_channel", "published"]
    list_filter = ["primary_channel", "published"]


@admin.register(DirectoryOrganisation)
class DirectoryOrganisationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "primary_channel", "published"]
    list_filter = ["primary_channel", "published"]


@admin.register(DirectoryVenue)
class DirectoryVenueAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "primary_channel", "published"]
    list_filter = ["primary_channel", "published"]
