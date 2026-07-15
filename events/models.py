"""Event content type mirroring LocalGov Drupal Events module."""

from django.db import models
from django.urls import reverse

from core.models import PublishableModel, Topic


class Event(PublishableModel):
    """Council event for the events listing."""

    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    image = models.ImageField(upload_to="events/", blank=True)
    topics = models.ManyToManyField(Topic, blank=True, related_name="events")

    class Meta:
        ordering = ["start_date"]

    def get_absolute_url(self):
        return reverse("events:event_detail", kwargs={"slug": self.slug})
