"""Unit tests for directory features."""

from django.test import TestCase
from django.urls import reverse

from directories.models import DirectoryChannel, DirectoryFacet, DirectoryFacetType, DirectoryOrganisation


class DirectoryTests(TestCase):
    def setUp(self):
        self.channel = DirectoryChannel.objects.create(
            title="Schools",
            slug="schools",
            summary="School directory",
        )
        facet_type = DirectoryFacetType.objects.create(name="Age", slug="age")
        self.facet = DirectoryFacet.objects.create(
            facet_type=facet_type, name="Primary", slug="primary"
        )
        self.channel.facets.add(self.facet)
        DirectoryOrganisation.objects.create(
            title="Example School",
            slug="example-school",
            primary_channel=self.channel,
            body="A primary school",
        )
        org = DirectoryOrganisation.objects.get(slug="example-school")
        org.facets.add(self.facet)

    def test_channel_list(self):
        response = self.client.get(reverse("directories:channel_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Schools")

    def test_channel_search(self):
        response = self.client.get(
            reverse("directories:channel_detail", kwargs={"slug": "schools"}),
            {"q": "Example"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Example School")

    def test_facet_filter(self):
        response = self.client.get(
            reverse("directories:channel_detail", kwargs={"slug": "schools"}),
            {"facet": "primary"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Example School")
