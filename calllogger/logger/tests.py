from django.test import TestCase
from logger.models import Call, CallStart


class CallTestCase(TestCase):
    def test_call_start(self):
        """
        It should create a CallStart record when a Call record is created.
        """
        Call.objects.create(
            source='123 456 789',
            destination='123 456 780'
        )
        self.assertNotEqual(0, CallStart.objects.count())
