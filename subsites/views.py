"""Subsite views."""

from django.views.generic import DetailView, ListView

from core.views import get_published_or_404
from subsites.models import SubsiteOverview, SubsitePage


class SubsiteOverviewListView(ListView):
    model = SubsiteOverview
    template_name = "subsites/overview_list.html"
    context_object_name = "subsites"

    def get_queryset(self):
        return SubsiteOverview.objects.filter(published=True)


class SubsiteOverviewDetailView(DetailView):
    model = SubsiteOverview
    template_name = "subsites/overview_detail.html"
    context_object_name = "subsite"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(SubsiteOverview, slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pages"] = self.object.pages.filter(published=True)
        return context


class SubsitePageDetailView(DetailView):
    model = SubsitePage
    template_name = "subsites/page_detail.html"
    context_object_name = "page"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(
            SubsitePage,
            slug=self.kwargs["slug"],
            subsite__slug=self.kwargs["subsite_slug"],
            subsite__published=True,
        )
