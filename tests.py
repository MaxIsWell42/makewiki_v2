import unittest

from django.test import TestCase, client
from django.contrib.auth.models import User
from wiki.models import Page

class WikiTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if true equals true """
        self.assertEqual(True, True)

class TestSlug(TestCase:)
    pass

class PageListViewTests(TestCase):
    ''' Test that the homepage works '''
    def test_multiple_pages(self):
        user = User.objects.create()

        Page.objects.create(title="My Test Page", content = 'test', author = user)
        Page.objects.create(title="Another Test Page", content = 'Another test', author = user)

    ''' Assures that the wiki details page loads a speicific page '''
    def test_specific_pages(self):
        Page.objects.create(title="Test title", content = "Test", author = user)
        self.assert(Page.objects.title = "Test title")

        response = self.client.get("/Test-title/")

        self.assertEqual(response.status_code, 200)
    # Todo: Make a test to check if the page creation form loads in /create


    