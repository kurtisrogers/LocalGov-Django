"""Service views."""

from django.views.generic import DetailView, ListView

from core.views import get_published_or_404
from services.models import ServiceLandingPage, ServicePage, ServiceStatus, ServiceSubLandingPage


class ServiceLandingListView(ListView):
    model = ServiceLandingPage
    template_name = "services/landing_list.html"
    context_object_name = "services"

    def get_queryset(self):
        return ServiceLandingPage.objects.filter(published=True)


class ServiceLandingDetailView(DetailView):
    model = ServiceLandingPage
    template_name = "services/landing_detail.html"
    context_object_name = "service"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(ServiceLandingPage, slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.object
        context["sub_landings"] = service.sub_landings.filter(published=True)
        context["pages"] = service.pages.filter(published=True, sub_landing__isnull=True)
        context["statuses"] = service.statuses.filter(published=True, active=True)
        return context


class ServiceSubLandingDetailView(DetailView):
    model = ServiceSubLandingPage
    template_name = "services/sub_landing_detail.html"
    context_object_name = "sub_landing"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(
            ServiceSubLandingPage,
            slug=self.kwargs["slug"],
            service__slug=self.kwargs["service_slug"],
            service__published=True,
        )


class ServicePageDetailView(DetailView):
    model = ServicePage
    template_name = "services/page_detail.html"
    context_object_name = "page"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(
            ServicePage,
            slug=self.kwargs["slug"],
            service__slug=self.kwargs["service_slug"],
            service__published=True,
        )


class ServiceStatusDetailView(DetailView):
    model = ServiceStatus
    template_name = "services/status_detail.html"
    context_object_name = "status"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(
            ServiceStatus,
            slug=self.kwargs["slug"],
            service__slug=self.kwargs["service_slug"],
            service__published=True,
        )
