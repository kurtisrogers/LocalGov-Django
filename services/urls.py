"""Service URL configuration."""

from django.urls import path

from services import views

app_name = "services"

urlpatterns = [
    path("", views.ServiceLandingListView.as_view(), name="landing_list"),
    path("<slug:slug>/", views.ServiceLandingDetailView.as_view(), name="landing_detail"),
    path(
        "<slug:service_slug>/<slug:slug>/",
        views.ServiceSubLandingDetailView.as_view(),
        name="sub_landing_detail",
    ),
    path(
        "<slug:service_slug>/page/<slug:slug>/",
        views.ServicePageDetailView.as_view(),
        name="page_detail",
    ),
    path(
        "<slug:service_slug>/status/<slug:slug>/",
        views.ServiceStatusDetailView.as_view(),
        name="status_detail",
    ),
]
