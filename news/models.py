"""News content types mirroring LocalGov Drupal News module."""

from django.db import models
from django.urls import reverse
from django.utils import timezone

from core.models import PublishableModel, Topic


class Newsroom(PublishableModel):
    """Page for listing and featuring news articles."""

    class Meta:
        verbose_name_plural = "Newsrooms"

    def get_absolute_url(self):
        return reverse("news:newsroom_detail", kwargs={"slug": self.slug})


class NewsArticle(PublishableModel):
    """Stand-alone news article."""

    newsroom = models.ForeignKey(
        Newsroom,
        on_delete=models.CASCADE,
        related_name="articles",
    )
    published_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to="news/", blank=True)
    featured = models.BooleanField(default=False)
    categories = models.ManyToManyField(Topic, blank=True, related_name="news_articles")
    related_articles = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False,
        related_name="related_to",
    )

    class Meta:
        ordering = ["-published_date", "title"]
        verbose_name = "News article"

    def get_absolute_url(self):
        return reverse(
            "news:article_detail",
            kwargs={
                "newsroom_slug": self.newsroom.slug,
                "year": self.published_date.year,
                "slug": self.slug,
            },
        )
