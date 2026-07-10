"""Unit tests for guide and step-by-step navigation."""

from django.test import TestCase
from django.urls import reverse

from guides.models import GuideOverview, GuidePage
from step_by_step.models import StepByStepOverview, StepByStepPage


class GuideNavigationTests(TestCase):
    def setUp(self):
        self.guide = GuideOverview.objects.create(
            title="Test Guide", slug="test-guide", body="Overview"
        )
        self.page1 = GuidePage.objects.create(
            title="Page 1", slug="page-1", guide=self.guide, order=1, body="First"
        )
        self.page2 = GuidePage.objects.create(
            title="Page 2", slug="page-2", guide=self.guide, order=2, body="Second"
        )

    def test_guide_page_navigation(self):
        self.assertEqual(self.page2.previous_page, self.page1)
        self.assertEqual(self.page1.next_page, self.page2)

    def test_guide_page_renders(self):
        response = self.client.get(
            reverse("guides:page_detail", kwargs={"guide_slug": "test-guide", "slug": "page-2"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Previous: Page 1")


class StepByStepTests(TestCase):
    def setUp(self):
        self.overview = StepByStepOverview.objects.create(
            title="Register a death", slug="register-a-death", body="Guide"
        )
        self.step1 = StepByStepPage.objects.create(
            title="Step 1", slug="step-1", overview=self.overview, step_number=1, body="First"
        )
        self.step2 = StepByStepPage.objects.create(
            title="Step 2", slug="step-2", overview=self.overview, step_number=2, body="Second"
        )

    def test_step_navigation(self):
        self.assertEqual(self.step2.previous_step, self.step1)
        self.assertEqual(self.step1.next_step, self.step2)

    def test_overview_renders(self):
        response = self.client.get(
            reverse("step_by_step:overview_detail", kwargs={"slug": "register-a-death"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Step 1")
