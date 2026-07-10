"""News URL configuration."""

from django.urls import path

from news import views

app_name = "news"

urlpatterns = [
    path("", views.NewsroomListView.as_view(), name="newsroom_list"),
    path("<slug:slug>/", views.NewsroomDetailView.as_view(), name="newsroom_detail"),
    path(
        "<slug:newsroom_slug>/<int:year>/<slug:slug>/",
        views.NewsArticleDetailView.as_view(),
        name="article_detail",
    ),
]
