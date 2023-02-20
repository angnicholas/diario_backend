from django.test import TestCase
# Create your tests here.

from django.urls import include, path, reverse
from rest_framework.test import APITestCase


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        self.assertEqual(1, 2)
