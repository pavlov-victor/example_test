from django.test import TestCase

from telegram.services import get_user_from_telegram


class SomeTest(TestCase):

    def test_get_user_from_telegram(self):
        assert get_user_from_telegram(2) == 1
