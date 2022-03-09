from django.test import TestCase
from django.urls import reverse


class ViewsTests(TestCase):
    def test_index(self):
        """
        Test `/api` returns success response.
        """

        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {
                "message": "Coding exercise solution",
                "available_paths": [
                    "/api",
                    "/api/hello-world",
                    "/api/add-numbers/<num_one>/<num_two>",
                ],
            },
        )

    def test_hello_world(self):
        """
        Test `/api/hello-world` returns success response.
        """

        response = self.client.get(reverse("hello-world"))

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"message": "Hello World"})

    def test_add_numbers_with_valid_numbers(self):
        """
        Test `/api/add-numbers/<num_one>/<num_two>` returns success response.
        """

        response = self.client.get(reverse("add-numbers", kwargs={"num_one": "2342", "num_two": "28"}))

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {
                "sum": 2370.0,
                "errors": None,
            },
        )

    def test_add_numbers_with_invalid_num_one(self):
        """
        Test `/api/add-numbers/<number_one>/<number_two>` returns error response.
        """

        response = self.client.get(reverse("add-numbers", kwargs={"num_one": "2(42.", "num_two": "28"}))

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(
            response.content,
            {
                "sum": None,
                "errors": [{"message": "Provided value 2(42. is not a valid number"}],
            },
        )

    def test_add_numbers_with_invalid_num_two(self):
        """
        Test `/api/add-numbers/<num_one>/<num_two>` returns error response.
        """

        response = self.client.get(reverse("add-numbers", kwargs={"num_one": "60", "num_two": "4ty"}))

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(
            response.content,
            {
                "sum": None,
                "errors": [{"message": "Provided value 4ty is not a valid number"}],
            },
        )

    def test_add_numbers_with_invalid_numbers(self):
        """
        Test `/api/add-numbers/<num_one>/<num_two>` returns error response.
        """

        response = self.client.get(reverse("add-numbers", kwargs={"num_one": "£453", "num_two": "<!>"}))

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(
            response.content,
            {
                "sum": None,
                "errors": [
                    {"message": "Provided value £453 is not a valid number"},
                    {"message": "Provided value <!> is not a valid number"},
                ],
            },
        )
