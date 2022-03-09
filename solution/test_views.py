from django.test import TestCase

from django.test import TestCase
from django.urls import reverse


class SolutionViewTests(TestCase):
    def test_index(self):
        """
        Test `/api` path returns the expected value.
        """

        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json(),
            {
                "message": "Coding exercise solution",
                "available_paths": [
                    "/api",
                    "/api/hello-world",
                ],
            },
        )

    def test_hello_world(self):
        """
        Test `/api/hello-world` returns the expected value.
        """

        response = self.client.get(reverse("hello-world"))

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {"message": "Hello World"})
