"""Directory content types mirroring LocalGov Drupal Directories module."""

from django.db import models
from django.urls import reverse

from core.models import PublishableModel, Topic


class DirectoryFacetType(models.Model):
    """Facet type grouping (e.g. Age, Location)."""

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class DirectoryFacet(models.Model):
    """Individual facet value for filtering directory items."""

    facet_type = models.ForeignKey(
        DirectoryFacetType,
        on_delete=models.CASCADE,
        related_name="facets",
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        unique_together = [("facet_type", "slug")]
        ordering = ["facet_type", "name"]

    def __str__(self) -> str:
        return f"{self.facet_type.name}: {self.name}"


class DirectoryChannel(PublishableModel):
    """Searchable/filterable directory listing page."""

    facets = models.ManyToManyField(DirectoryFacet, blank=True, related_name="channels")
    topics = models.ManyToManyField(Topic, blank=True, related_name="directory_channels")

    class Meta:
        verbose_name = "Directory channel"

    def get_absolute_url(self):
        return reverse("directories:channel_detail", kwargs={"slug": self.slug})


class DirectoryEntryBase(PublishableModel):
    """Shared fields for directory item types."""

    primary_channel = models.ForeignKey(
        DirectoryChannel,
        on_delete=models.CASCADE,
        related_name="%(class)s_entries",
    )
    other_channels = models.ManyToManyField(
        DirectoryChannel,
        blank=True,
        related_name="%(class)s_other_entries",
    )
    facets = models.ManyToManyField(DirectoryFacet, blank=True, related_name="%(class)s_entries")
    topics = models.ManyToManyField(Topic, blank=True, related_name="%(class)s_entries")

    class Meta:
        abstract = True

    def get_channel_slug(self):
        return self.primary_channel.slug


class DirectoryPage(DirectoryEntryBase):
    """General-purpose directory entry."""

    class Meta:
        verbose_name = "Directory page"

    def get_absolute_url(self):
        return reverse(
            "directories:page_detail",
            kwargs={"channel_slug": self.get_channel_slug(), "slug": self.slug},
        )


class DirectoryOrganisation(DirectoryEntryBase):
    """Organisation entry (libraries, schools, etc.)."""

    address = models.TextField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name = "Directory organisation"

    def get_absolute_url(self):
        return reverse(
            "directories:organisation_detail",
            kwargs={"channel_slug": self.get_channel_slug(), "slug": self.slug},
        )


class DirectoryVenue(DirectoryEntryBase):
    """Venue entry with location (parks, sports facilities)."""

    address = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    opening_hours = models.TextField(blank=True)

    class Meta:
        verbose_name = "Directory venue"

    def get_absolute_url(self):
        return reverse(
            "directories:venue_detail",
            kwargs={"channel_slug": self.get_channel_slug(), "slug": self.slug},
        )
