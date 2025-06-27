from django.test import TestCase
from django.db import IntegrityError
from ...models import FAQ, UserSubscription


class FAQModelTest(TestCase):
    def test_create_faq(self):
        faq = FAQ.objects.create(
            question="How to place an order?",
            answer="Click on the product and add to cart."
        )
        self.assertEqual(faq.question, "How to place an order?")
        self.assertEqual(faq.answer, "Click on the product and add to cart.")


class UserSubscriptionModelTest(TestCase):
    def test_create_subscription(self):
        subscription = UserSubscription.objects.create(
            user_id=12345
        )
        self.assertEqual(subscription.user_id, 12345)
        self.assertFalse(subscription.is_subscribed)

    def test_subscribe_user(self):
        subscription = UserSubscription.objects.create(
            user_id=12345,
            is_subscribed=True
        )
        self.assertTrue(subscription.is_subscribed)

    def test_unique_user_subscription(self):
        UserSubscription.objects.create(user_id=12345)
        with self.assertRaises(IntegrityError):
            UserSubscription.objects.create(user_id=12345)
