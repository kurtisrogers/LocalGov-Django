"""Event views."""

from django.views.generic import DetailView, ListView

from core.views import get_published_or_404
from events.models import Event


class EventListView(ListView):
    model = Event
    template_name = "events/event_list.html"
    context_object_name = "events"

    def get_queryset(self):
        return Event.objects.filter(published=True)


class EventDetailView(DetailView):
    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"
    slug_field = "slug"

    def get_object(self):
        return get_published_or_404(Event, slug=self.kwargs["slug"])
