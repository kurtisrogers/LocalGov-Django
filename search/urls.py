"""Search URL configuration."""

from django.urls import path

from search import views

app_name = "search"

urlpatterns = [
    path("", views.SitewideSearchView.as_view(), name="sitewide"),
]
