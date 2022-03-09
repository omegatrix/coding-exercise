from django.test import TestCase
from django.urls import reverse

from .utils import string_to_float


class UtilTests(TestCase):
    def test_alphabet_chars(self):
        """
        Test non numerics.
        """

        result = string_to_float("qwe")

        self.assertIsNone(result)

    def test_int(self):
        """
        Test integers.
        """

        result = string_to_float("123")

        self.assertEqual(result, 123.0)

    def test_negative_numeric(self):
        """
        Test negatives.
        """

        result = string_to_float("-647.9463")

        self.assertEqual(result, -647.9463)

    def test_positive_numeric(self):
        """
        Test positive floats with `+` sign.
        """

        result = string_to_float("+475.99")

        self.assertEqual(result, 475.99)
