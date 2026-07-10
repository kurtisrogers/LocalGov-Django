"""Step by step URL configuration."""

from django.urls import path

from step_by_step import views

app_name = "step_by_step"

urlpatterns = [
    path("", views.StepByStepOverviewListView.as_view(), name="overview_list"),
    path("<slug:slug>/", views.StepByStepOverviewDetailView.as_view(), name="overview_detail"),
    path(
        "<slug:overview_slug>/<slug:slug>/",
        views.StepByStepPageDetailView.as_view(),
        name="step_detail",
    ),
]
