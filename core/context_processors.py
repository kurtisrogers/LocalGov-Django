"""Template context processors."""

from django.conf import settings

from alerts.models import AlertBanner
from core.models import MenuItem, SiteConfiguration


def site_context(request):
    """Inject site-wide navigation and configuration."""
    site = SiteConfiguration.get_solo()
    return {
        "site_config": site,
        "primary_menu": MenuItem.objects.filter(menu_type=MenuItem.MenuType.PRIMARY),
        "secondary_menu": MenuItem.objects.filter(menu_type=MenuItem.MenuType.SECONDARY),
        "footer_menu": MenuItem.objects.filter(menu_type=MenuItem.MenuType.FOOTER),
        "mobile_breakpoint": settings.LOCALGOV_MOBILE_BREAKPOINT,
        "active_alerts": AlertBanner.objects.filter(active=True).order_by("-created"),
    }
