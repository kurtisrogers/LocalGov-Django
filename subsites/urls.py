"""Subsite URL configuration."""

from django.urls import path

from subsites import views

app_name = "subsites"

urlpatterns = [
    path("", views.SubsiteOverviewListView.as_view(), name="overview_list"),
    path("<slug:slug>/", views.SubsiteOverviewDetailView.as_view(), name="overview_detail"),
    path(
        "<slug:subsite_slug>/<slug:slug>/",
        views.SubsitePageDetailView.as_view(),
        name="page_detail",
    ),
]
