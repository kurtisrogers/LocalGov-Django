"""Sitewide search views."""

from django.db.models import Q
from django.views.generic import ListView

from directories.models import DirectoryChannel, DirectoryOrganisation, DirectoryPage, DirectoryVenue
from events.models import Event
from guides.models import GuideOverview
from news.models import NewsArticle
from services.models import ServiceLandingPage, ServicePage
from step_by_step.models import StepByStepOverview


class SitewideSearchView(ListView):
    template_name = "search/results.html"
    context_object_name = "results"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q", "").strip()
        if not query:
            return []

        results = []
        models = [
            (ServiceLandingPage, "Service"),
            (ServicePage, "Service page"),
            (GuideOverview, "Guide"),
            (StepByStepOverview, "Step by step"),
            (NewsArticle, "News"),
            (Event, "Event"),
            (DirectoryChannel, "Directory"),
            (DirectoryPage, "Directory page"),
            (DirectoryOrganisation, "Organisation"),
            (DirectoryVenue, "Venue"),
        ]
        for model, label in models:
            qs = model.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query) | Q(summary__icontains=query),
                published=True,
            )[:5]
            for obj in qs:
                results.append({"object": obj, "type": label})

        return results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "").strip()
        return context
