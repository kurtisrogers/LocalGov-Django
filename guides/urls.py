"""Guide URL configuration."""

from django.urls import path

from guides import views

app_name = "guides"

urlpatterns = [
    path("", views.GuideOverviewListView.as_view(), name="overview_list"),
    path("<slug:slug>/", views.GuideOverviewDetailView.as_view(), name="overview_detail"),
    path(
        "<slug:guide_slug>/<slug:slug>/",
        views.GuidePageDetailView.as_view(),
        name="page_detail",
    ),
]
