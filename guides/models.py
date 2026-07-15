"""Guide content types mirroring LocalGov Drupal Guides module."""

from django.db import models
from django.urls import reverse

from core.models import PublishableModel


class GuideOverview(PublishableModel):
    """Main page for a collection of connected guide pages."""

    class Meta:
        verbose_name = "Guide overview"
        verbose_name_plural = "Guide overviews"

    def get_absolute_url(self):
        return reverse("guides:overview_detail", kwargs={"slug": self.slug})


class GuidePage(PublishableModel):
    """Single page within a guide."""

    guide = models.ForeignKey(
        GuideOverview,
        on_delete=models.CASCADE,
        related_name="pages",
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["guide", "order"]
        verbose_name = "Guide page"

    def get_absolute_url(self):
        return reverse(
            "guides:page_detail",
            kwargs={"guide_slug": self.guide.slug, "slug": self.slug},
        )

    @property
    def previous_page(self):
        return (
            self.guide.pages.filter(order__lt=self.order).order_by("-order").first()
        )

    @property
    def next_page(self):
        return (
            self.guide.pages.filter(order__gt=self.order).order_by("order").first()
        )
