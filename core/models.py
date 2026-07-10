"""Shared models for LocalGov Django."""

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from model_utils.models import TimeStampedModel


class PublishableModel(TimeStampedModel):
    """Base model for published LocalGov content."""

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.TextField(blank=True)
    body = models.TextField(blank=True)
    published = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Topic(models.Model):
    """Taxonomy term for categorising content (LocalGov Topics vocabulary)."""

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class SiteConfiguration(models.Model):
    """Council site identity and global settings."""

    site_name = models.CharField(max_length=255, default="LocalGov Django")
    site_slogan = models.CharField(max_length=255, blank=True)
    council_name = models.CharField(max_length=255, default="Example Council")
    logo = models.ImageField(upload_to="site/", blank=True)
    primary_phone = models.CharField(max_length=50, blank=True)
    primary_email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    class Meta:
        verbose_name = "Site configuration"

    def __str__(self) -> str:
        return self.site_name

    @classmethod
    def get_solo(cls) -> "SiteConfiguration":
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class MenuItem(models.Model):
    """Navigation menu item for primary or secondary menus."""

    class MenuType(models.TextChoices):
        PRIMARY = "primary", "Primary navigation"
        SECONDARY = "secondary", "Services menu"
        FOOTER = "footer", "Footer"

    label = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    menu_type = models.CharField(max_length=20, choices=MenuType.choices)
    order = models.PositiveIntegerField(default=0)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children",
    )

    class Meta:
        ordering = ["menu_type", "order", "label"]

    def __str__(self) -> str:
        return f"{self.get_menu_type_display()}: {self.label}"
