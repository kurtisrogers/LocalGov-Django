"""Guide views."""

from django.views.generic import DetailView, ListView

from core.views import get_published_or_404
from guides.models import GuideOverview, GuidePage


class GuideOverviewListView(ListView):
    model = GuideOverview
    template_name = "guides/overview_list.html"
    context_object_name = "guides"

    def get_queryset(self):
        return GuideOverview.objects.filter(published=True)


class GuideOverviewDetailView(DetailView):
    model = GuideOverview
    template_name = "guides/overview_detail.html"
    context_object_name = "guide"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(GuideOverview, slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pages"] = self.object.pages.filter(published=True)
        return context


class GuidePageDetailView(DetailView):
    model = GuidePage
    template_name = "guides/page_detail.html"
    context_object_name = "page"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(
            GuidePage,
            slug=self.kwargs["slug"],
            guide__slug=self.kwargs["guide_slug"],
            guide__published=True,
        )
