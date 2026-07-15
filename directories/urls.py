"""Directory URL configuration."""

from django.urls import path

from directories import views

app_name = "directories"

urlpatterns = [
    path("", views.DirectoryChannelListView.as_view(), name="channel_list"),
    path("<slug:slug>/", views.DirectoryChannelDetailView.as_view(), name="channel_detail"),
    path(
        "<slug:channel_slug>/page/<slug:slug>/",
        views.DirectoryPageDetailView.as_view(),
        name="page_detail",
    ),
    path(
        "<slug:channel_slug>/organisation/<slug:slug>/",
        views.DirectoryOrganisationDetailView.as_view(),
        name="organisation_detail",
    ),
    path(
        "<slug:channel_slug>/venue/<slug:slug>/",
        views.DirectoryVenueDetailView.as_view(),
        name="venue_detail",
    ),
]
