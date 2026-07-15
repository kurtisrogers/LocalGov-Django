"""Step by step views."""

from django.views.generic import DetailView, ListView

from core.views import get_published_or_404
from step_by_step.models import StepByStepOverview, StepByStepPage


class StepByStepOverviewListView(ListView):
    model = StepByStepOverview
    template_name = "step_by_step/overview_list.html"
    context_object_name = "overviews"

    def get_queryset(self):
        return StepByStepOverview.objects.filter(published=True)


class StepByStepOverviewDetailView(DetailView):
    model = StepByStepOverview
    template_name = "step_by_step/overview_detail.html"
    context_object_name = "overview"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(StepByStepOverview, slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["steps"] = self.object.steps.filter(published=True)
        return context


class StepByStepPageDetailView(DetailView):
    model = StepByStepPage
    template_name = "step_by_step/step_detail.html"
    context_object_name = "step"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(
            StepByStepPage,
            slug=self.kwargs["slug"],
            overview__slug=self.kwargs["overview_slug"],
            overview__published=True,
        )
