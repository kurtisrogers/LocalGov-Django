"""Subsite content types mirroring LocalGov Drupal Subsites module."""

from django.db import models
from django.urls import reverse

from core.models import PublishableModel


class SubsiteOverview(PublishableModel):
    """Landing page for a council subsite."""

    domain = models.CharField(max_length=255, blank=True, help_text="Optional subsite domain")
    featured_image = models.ImageField(upload_to="subsites/", blank=True)

    class Meta:
        verbose_name = "Subsite overview"
        verbose_name_plural = "Subsite overviews"

    def get_absolute_url(self):
        return reverse("subsites:overview_detail", kwargs={"slug": self.slug})


class SubsitePage(PublishableModel):
    """Child page within a subsite."""

    subsite = models.ForeignKey(
        SubsiteOverview,
        on_delete=models.CASCADE,
        related_name="pages",
    )

    class Meta:
        verbose_name = "Subsite page"

    def get_absolute_url(self):
        return reverse(
            "subsites:page_detail",
            kwargs={"subsite_slug": self.subsite.slug, "slug": self.slug},
        )
