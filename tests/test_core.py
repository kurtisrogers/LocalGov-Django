"""Unit tests for LocalGov Django."""

from django.test import TestCase
from django.urls import reverse

from core.models import MenuItem, SiteConfiguration, Topic
from services.models import ServiceLandingPage


class SiteConfigurationTests(TestCase):
    def test_singleton_returns_same_instance(self):
        first = SiteConfiguration.get_solo()
        second = SiteConfiguration.get_solo()
        self.assertEqual(first.pk, second.pk)


class HomePageTests(TestCase):
    def test_homepage_returns_200(self):
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "LocalGov Django")


class ServicesTests(TestCase):
    def setUp(self):
        self.service = ServiceLandingPage.objects.create(
            title="Waste and recycling",
            slug="waste-recycling",
            summary="Bin collections",
            body="Content",
        )

    def test_service_list_page(self):
        response = self.client.get(reverse("services:landing_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Waste and recycling")

    def test_service_detail_page(self):
        response = self.client.get(
            reverse("services:landing_detail", kwargs={"slug": "waste-recycling"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bin collections")

    def test_unpublished_service_returns_404(self):
        self.service.published = False
        self.service.save()
        response = self.client.get(
            reverse("services:landing_detail", kwargs={"slug": "waste-recycling"})
        )
        self.assertEqual(response.status_code, 404)


class SearchTests(TestCase):
    def setUp(self):
        ServiceLandingPage.objects.create(
            title="Council tax",
            slug="council-tax",
            summary="Pay council tax",
            body="Payment options",
        )

    def test_search_finds_content(self):
        response = self.client.get(reverse("search:sitewide"), {"q": "council tax"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Council tax")


class TopicTests(TestCase):
    def test_topic_slug_auto_generated(self):
        topic = Topic.objects.create(name="Environment")
        self.assertEqual(topic.slug, "environment")


class MenuTests(TestCase):
    def test_menu_items_ordered(self):
        MenuItem.objects.create(label="B", menu_type=MenuItem.MenuType.PRIMARY, url="/b/", order=2)
        MenuItem.objects.create(label="A", menu_type=MenuItem.MenuType.PRIMARY, url="/a/", order=1)
        items = list(MenuItem.objects.filter(menu_type=MenuItem.MenuType.PRIMARY))
        self.assertEqual(items[0].label, "A")
