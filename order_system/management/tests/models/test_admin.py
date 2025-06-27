from django.test import TestCase
from ...models import BroadcastMessage


class BroadcastMessageModelTest(TestCase):
    def test_create_broadcast_message(self):
        message = BroadcastMessage.objects.create(
            message="Welcome to our store!"
        )
        self.assertEqual(message.message, "Welcome to our store!")
        self.assertFalse(message.sent)
        self.assertIsNotNone(message.created_at)

    def test_mark_message_as_sent(self):
        message = BroadcastMessage.objects.create(
            message="Test message",
            sent=True
        )
        self.assertTrue(message.sent)
