"""URL configuration for LocalGov Django."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("services/", include("services.urls")),
    path("directories/", include("directories.urls")),
    path("guides/", include("guides.urls")),
    path("step-by-step/", include("step_by_step.urls")),
    path("news/", include("news.urls")),
    path("events/", include("events.urls")),
    path("subsites/", include("subsites.urls")),
    path("search/", include("search.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
