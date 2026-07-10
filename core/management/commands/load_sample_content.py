"""Load sample LocalGov Django content for development and demos."""

from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from alerts.models import AlertBanner
from core.models import MenuItem, SiteConfiguration, Topic
from directories.models import DirectoryChannel, DirectoryFacet, DirectoryFacetType, DirectoryOrganisation
from events.models import Event
from guides.models import GuideOverview, GuidePage
from news.models import NewsArticle, Newsroom
from services.models import ServiceLandingPage, ServicePage, ServiceStatus, ServiceSubLandingPage
from step_by_step.models import StepByStepOverview, StepByStepPage
from subsites.models import SubsiteOverview, SubsitePage


class Command(BaseCommand):
    help = "Load sample content mirroring LocalGov Drupal demo data"

    def handle(self, *args, **options):
        site = SiteConfiguration.get_solo()
        site.site_name = "LocalGov Django"
        site.site_slogan = "Open source publishing for local government"
        site.council_name = "Example Council"
        site.primary_phone = "01234 567890"
        site.primary_email = "hello@examplecouncil.gov.uk"
        site.address = "Town Hall\nExample Town\nEX1 2PL"
        site.save()

        self._create_menus()
        self._create_topics()
        self._create_alerts()
        self._create_services()
        self._create_directories()
        self._create_guides()
        self._create_step_by_step()
        self._create_news()
        self._create_events()
        self._create_subsites()
        self.stdout.write(self.style.SUCCESS("Sample LocalGov content loaded."))

    def _create_menus(self):
        menus = [
            ("Home", "/", MenuItem.MenuType.PRIMARY, 0),
            ("Services", "/services/", MenuItem.MenuType.PRIMARY, 1),
            ("News", "/news/", MenuItem.MenuType.PRIMARY, 2),
            ("Events", "/events/", MenuItem.MenuType.PRIMARY, 3),
            ("Directories", "/directories/", MenuItem.MenuType.PRIMARY, 4),
            ("Bin collection", "/services/waste-recycling/", MenuItem.MenuType.SECONDARY, 0),
            ("Council tax", "/services/council-tax/", MenuItem.MenuType.SECONDARY, 1),
            ("Housing", "/services/housing/", MenuItem.MenuType.SECONDARY, 2),
            ("Accessibility", "#", MenuItem.MenuType.FOOTER, 0),
            ("Privacy", "#", MenuItem.MenuType.FOOTER, 1),
        ]
        for label, url, menu_type, order in menus:
            MenuItem.objects.get_or_create(
                label=label,
                menu_type=menu_type,
                defaults={"url": url, "order": order},
            )

    def _create_topics(self):
        for name in ["Council", "Community", "Environment", "Housing"]:
            Topic.objects.get_or_create(name=name, defaults={"slug": name.lower()})

    def _create_alerts(self):
        AlertBanner.objects.get_or_create(
            slug="major-road-closure",
            defaults={
                "title": "Major road closure on High Street",
                "summary": "High Street will be closed until Friday for emergency repairs.",
                "alert_type": AlertBanner.Type.MAJOR,
                "active": True,
            },
        )

    def _create_services(self):
        waste, _ = ServiceLandingPage.objects.get_or_create(
            slug="waste-recycling",
            defaults={
                "title": "Waste and recycling",
                "summary": "Bin collections, recycling centres, and bulky waste.",
                "body": "Find out when your bins are collected and how to recycle.",
            },
        )
        tax, _ = ServiceLandingPage.objects.get_or_create(
            slug="council-tax",
            defaults={
                "title": "Council tax",
                "summary": "Pay your council tax, apply for discounts, and manage your account.",
                "body": "Council tax funds local services including schools, roads, and social care.",
            },
        )
        ServiceLandingPage.objects.get_or_create(
            slug="housing",
            defaults={
                "title": "Housing",
                "summary": "Council housing, homelessness support, and private rented sector.",
                "body": "Housing advice and support for residents.",
            },
        )
        sub, _ = ServiceSubLandingPage.objects.get_or_create(
            slug="bin-collections",
            service=waste,
            defaults={
                "title": "Bin collections",
                "summary": "Collection days and missed bin reporting.",
                "order": 1,
            },
        )
        ServicePage.objects.get_or_create(
            slug="check-collection-day",
            service=waste,
            sub_landing=sub,
            defaults={
                "title": "Check your collection day",
                "summary": "Find out when your bins are collected.",
                "body": "Enter your postcode to find your collection schedule.",
            },
        )
        ServiceStatus.objects.get_or_create(
            slug="garden-waste-suspension",
            service=waste,
            defaults={
                "title": "Garden waste collections suspended",
                "summary": "Garden waste collections are suspended due to staff shortages.",
                "body": "We apologise for the inconvenience. Normal service will resume as soon as possible.",
                "severity": ServiceStatus.Severity.MINOR,
                "active": True,
            },
        )
        ServicePage.objects.get_or_create(
            slug="pay-council-tax",
            service=tax,
            defaults={
                "title": "Pay your council tax",
                "summary": "Pay online, by direct debit, or at the post office.",
                "body": "You can pay your council tax in monthly instalments or as a single payment.",
            },
        )

    def _create_directories(self):
        age_type, _ = DirectoryFacetType.objects.get_or_create(
            slug="age", defaults={"name": "Age"}
        )
        primary, _ = DirectoryFacet.objects.get_or_create(
            facet_type=age_type, slug="primary", defaults={"name": "Primary"}
        )
        secondary, _ = DirectoryFacet.objects.get_or_create(
            facet_type=age_type, slug="secondary", defaults={"name": "Secondary"}
        )
        channel, _ = DirectoryChannel.objects.get_or_create(
            slug="schools",
            defaults={
                "title": "Schools directory",
                "summary": "Find schools in the borough.",
                "body": "Search and filter schools by age and location.",
            },
        )
        channel.facets.set([primary, secondary])
        DirectoryOrganisation.objects.get_or_create(
            slug="example-primary-school",
            primary_channel=channel,
            defaults={
                "title": "Example Primary School",
                "summary": "Community primary school for ages 4-11.",
                "body": "A welcoming primary school in the heart of the community.",
                "address": "1 School Lane, Example Town",
                "phone": "01234 567001",
            },
        )

    def _create_guides(self):
        guide, _ = GuideOverview.objects.get_or_create(
            slug="animal-welfare-licences",
            defaults={
                "title": "Animal welfare licences",
                "summary": "Guidance on applying for animal welfare licences.",
                "body": "This guide covers the types of licence and how to apply.",
            },
        )
        GuidePage.objects.get_or_create(
            slug="do-you-need-a-licence",
            guide=guide,
            defaults={
                "title": "Do you need a licence?",
                "order": 1,
                "body": "You may need a licence if you run a business involving animals.",
            },
        )
        GuidePage.objects.get_or_create(
            slug="how-to-apply",
            guide=guide,
            defaults={
                "title": "How to apply",
                "order": 2,
                "body": "Complete the online application form and pay the fee.",
            },
        )

    def _create_step_by_step(self):
        overview, _ = StepByStepOverview.objects.get_or_create(
            slug="register-a-death",
            defaults={
                "title": "Register a death",
                "summary": "Step by step guide to registering a death.",
                "body": "You must register a death within five days.",
            },
        )
        StepByStepPage.objects.get_or_create(
            slug="book-appointment",
            overview=overview,
            defaults={
                "title": "Book an appointment",
                "step_number": 1,
                "body": "Contact the register office to book an appointment.",
            },
        )
        StepByStepPage.objects.get_or_create(
            slug="bring-documents",
            overview=overview,
            defaults={
                "title": "Bring the required documents",
                "step_number": 2,
                "body": "Bring the medical certificate of cause of death and identification.",
            },
        )

    def _create_news(self):
        newsroom, _ = Newsroom.objects.get_or_create(
            slug="news",
            defaults={"title": "News", "summary": "Latest news from Example Council."},
        )
        NewsArticle.objects.get_or_create(
            slug="council-approves-climate-plan",
            newsroom=newsroom,
            defaults={
                "title": "Council approves climate action plan",
                "summary": "Example Council has approved an ambitious climate action plan.",
                "body": "The plan sets targets for net zero emissions by 2030.",
                "featured": True,
            },
        )

    def _create_events(self):
        Event.objects.get_or_create(
            slug="summer-fete",
            defaults={
                "title": "Summer fete",
                "summary": "Annual summer fete in the town park.",
                "body": "Join us for games, food stalls, and live music.",
                "start_date": timezone.now() + timedelta(days=30),
                "location": "Town Park",
            },
        )

    def _create_subsites(self):
        subsite, _ = SubsiteOverview.objects.get_or_create(
            slug="libraries",
            defaults={
                "title": "Libraries",
                "summary": "Library services across the borough.",
                "body": "Find your local library and explore our services.",
            },
        )
        SubsitePage.objects.get_or_create(
            slug="join-the-library",
            subsite=subsite,
            defaults={
                "title": "Join the library",
                "body": "Anyone living in the borough can join for free.",
            },
        )
