"""Shared view utilities."""

from django.http import Http404
from django.shortcuts import get_object_or_404


def get_published_or_404(model, **kwargs):
    """Return a published object or raise 404."""
    obj = get_object_or_404(model, **kwargs)
    if hasattr(obj, "published") and not obj.published:
        raise Http404()
    return obj
