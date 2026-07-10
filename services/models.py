"""Service content types mirroring LocalGov Drupal Services module."""

from django.db import models
from django.urls import reverse

from core.models import PublishableModel, Topic


class ServiceLandingPage(PublishableModel):
    """Top-level section for each council service."""

    topics = models.ManyToManyField(Topic, blank=True, related_name="service_landings")
    featured_image = models.ImageField(upload_to="services/", blank=True)

    class Meta:
        verbose_name = "Service landing page"

    def get_absolute_url(self):
        return reverse("services:landing_detail", kwargs={"slug": self.slug})


class ServiceSubLandingPage(PublishableModel):
    """Index page linking to pages within a service."""

    service = models.ForeignKey(
        ServiceLandingPage,
        on_delete=models.CASCADE,
        related_name="sub_landings",
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["service", "order", "title"]
        verbose_name = "Service sub-landing page"

    def get_absolute_url(self):
        return reverse(
            "services:sub_landing_detail",
            kwargs={"service_slug": self.service.slug, "slug": self.slug},
        )


class ServicePage(PublishableModel):
    """Basic page placed within a service hierarchy."""

    service = models.ForeignKey(
        ServiceLandingPage,
        on_delete=models.CASCADE,
        related_name="pages",
    )
    sub_landing = models.ForeignKey(
        ServiceSubLandingPage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pages",
    )
    topics = models.ManyToManyField(Topic, blank=True, related_name="service_pages")

    class Meta:
        verbose_name = "Service page"

    def get_absolute_url(self):
        return reverse(
            "services:page_detail",
            kwargs={"service_slug": self.service.slug, "slug": self.slug},
        )


class ServiceStatus(PublishableModel):
    """Status update for a council service."""

    class Severity(models.TextChoices):
        MINOR = "minor", "Minor"
        MAJOR = "major", "Major"
        ANNOUNCEMENT = "announcement", "Announcement"
        NOTABLE_PERSON = "notable_person", "Notable person"

    service = models.ForeignKey(
        ServiceLandingPage,
        on_delete=models.CASCADE,
        related_name="statuses",
    )
    severity = models.CharField(
        max_length=20,
        choices=Severity.choices,
        default=Severity.MINOR,
    )
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Service statuses"

    def get_absolute_url(self):
        return reverse(
            "services:status_detail",
            kwargs={"service_slug": self.service.slug, "slug": self.slug},
        )
