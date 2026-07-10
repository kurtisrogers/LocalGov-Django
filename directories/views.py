"""Directory views."""

from django.db.models import Q
from django.views.generic import DetailView, ListView

from core.views import get_published_or_404
from directories.models import (
    DirectoryChannel,
    DirectoryOrganisation,
    DirectoryPage,
    DirectoryVenue,
)


class DirectoryChannelListView(ListView):
    model = DirectoryChannel
    template_name = "directories/channel_list.html"
    context_object_name = "channels"

    def get_queryset(self):
        return DirectoryChannel.objects.filter(published=True)


class DirectoryChannelDetailView(DetailView):
    model = DirectoryChannel
    template_name = "directories/channel_detail.html"
    context_object_name = "channel"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(DirectoryChannel, slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        channel = self.object
        query = self.request.GET.get("q", "").strip()
        facet_slug = self.request.GET.get("facet", "")

        pages = DirectoryPage.objects.filter(primary_channel=channel, published=True)
        orgs = DirectoryOrganisation.objects.filter(primary_channel=channel, published=True)
        venues = DirectoryVenue.objects.filter(primary_channel=channel, published=True)

        if query:
            pages = pages.filter(Q(title__icontains=query) | Q(body__icontains=query))
            orgs = orgs.filter(Q(title__icontains=query) | Q(body__icontains=query))
            venues = venues.filter(Q(title__icontains=query) | Q(body__icontains=query))

        if facet_slug:
            pages = pages.filter(facets__slug=facet_slug)
            orgs = orgs.filter(facets__slug=facet_slug)
            venues = venues.filter(facets__slug=facet_slug)

        context["directory_pages"] = pages.distinct()
        context["organisations"] = orgs.distinct()
        context["venues"] = venues.distinct()
        context["search_query"] = query
        context["selected_facet"] = facet_slug
        context["facets"] = channel.facets.all()
        return context


class DirectoryPageDetailView(DetailView):
    model = DirectoryPage
    template_name = "directories/page_detail.html"
    context_object_name = "entry"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(
            DirectoryPage,
            slug=self.kwargs["slug"],
            primary_channel__slug=self.kwargs["channel_slug"],
            primary_channel__published=True,
        )


class DirectoryOrganisationDetailView(DetailView):
    model = DirectoryOrganisation
    template_name = "directories/organisation_detail.html"
    context_object_name = "entry"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(
            DirectoryOrganisation,
            slug=self.kwargs["slug"],
            primary_channel__slug=self.kwargs["channel_slug"],
            primary_channel__published=True,
        )


class DirectoryVenueDetailView(DetailView):
    model = DirectoryVenue
    template_name = "directories/venue_detail.html"
    context_object_name = "entry"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(
            DirectoryVenue,
            slug=self.kwargs["slug"],
            primary_channel__slug=self.kwargs["channel_slug"],
            primary_channel__published=True,
        )
