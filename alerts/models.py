"""Alert banner content type mirroring LocalGov Drupal Alert Banners module."""

from django.db import models

from core.models import PublishableModel


class AlertBanner(PublishableModel):
    """Site-wide or service-specific alert banner."""

    class Type(models.TextChoices):
        ANNOUNCEMENT = "announce", "Announcement"
        MINOR = "minor", "Minor"
        MAJOR = "major", "Major"
        NOTABLE_PERSON = "notable-person", "Notable person"

    alert_type = models.CharField(
        max_length=20,
        choices=Type.choices,
        default=Type.ANNOUNCEMENT,
    )
    active = models.BooleanField(default=True)
    link_url = models.URLField(blank=True)
    link_text = models.CharField(max_length=100, blank=True, default="More information")

    class Meta:
        ordering = ["-created"]
        verbose_name = "Alert banner"

    def __str__(self) -> str:
        return self.title
