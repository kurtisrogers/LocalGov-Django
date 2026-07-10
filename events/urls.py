"""Event URL configuration."""

from django.urls import path

from events import views

app_name = "events"

urlpatterns = [
    path("", views.EventListView.as_view(), name="event_list"),
    path("<slug:slug>/", views.EventDetailView.as_view(), name="event_detail"),
]
