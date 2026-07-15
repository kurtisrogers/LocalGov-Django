"""Homepage views."""

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        from events.models import Event
        from news.models import NewsArticle
        from services.models import ServiceLandingPage

        context = super().get_context_data(**kwargs)
        context["featured_services"] = ServiceLandingPage.objects.filter(published=True)[:6]
        context["latest_news"] = NewsArticle.objects.filter(published=True)[:3]
        context["upcoming_events"] = Event.objects.filter(published=True)[:3]
        return context
