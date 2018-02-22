from django.test import TestCase
from logger.models import Call, CallStart, CallEnd


class CallTestCase(TestCase):
    def test_call_start(self):
        """
        It should create a CallStart record when a Call record is created.
        """
        Call.objects.create(
            source='123 456 789',
            destination='123 456 780'
        )
        self.assertEqual(1, CallStart.objects.count())

    def test_call_end(self):
        """
        It should create a CallEnd record when a Call record's end_call is called.
        """
        call = Call.objects.create(
            source='123 456 789',
            destination='123 456 780'
        )
        call.end_call()
        self.assertEqual(1, CallStart.objects.count())
        self.assertEqual(1, CallEnd.objects.count())

        # should not create another record if the method is called again
        call.end_call()
        self.assertEqual(1, CallEnd.objects.count())
