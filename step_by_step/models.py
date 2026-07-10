"""Step by step content types mirroring LocalGov Drupal Step by Step module."""

from django.db import models
from django.urls import reverse

from core.models import PublishableModel


class StepByStepOverview(PublishableModel):
    """Main page for a sequential step-by-step process."""

    class Meta:
        verbose_name = "Step by step overview"
        verbose_name_plural = "Step by step overviews"

    def get_absolute_url(self):
        return reverse("step_by_step:overview_detail", kwargs={"slug": self.slug})


class StepByStepPage(PublishableModel):
    """Single step within a step-by-step process."""

    overview = models.ForeignKey(
        StepByStepOverview,
        on_delete=models.CASCADE,
        related_name="steps",
    )
    step_number = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["overview", "step_number"]
        verbose_name = "Step by step page"
        unique_together = [("overview", "step_number")]

    def get_absolute_url(self):
        return reverse(
            "step_by_step:step_detail",
            kwargs={"overview_slug": self.overview.slug, "slug": self.slug},
        )

    @property
    def previous_step(self):
        return (
            self.overview.steps.filter(step_number__lt=self.step_number)
            .order_by("-step_number")
            .first()
        )

    @property
    def next_step(self):
        return (
            self.overview.steps.filter(step_number__gt=self.step_number)
            .order_by("step_number")
            .first()
        )
