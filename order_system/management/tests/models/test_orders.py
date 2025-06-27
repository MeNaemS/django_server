from django.test import TestCase
from decimal import Decimal
from ...models import Category, Product, Order, OrderItem


class OrderModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Test Product",
            price=Decimal('100.00'),
            category=self.category
        )

    def test_create_order(self):
        order = Order.objects.create(
            user_id=12345,
            full_name="John Doe",
            address="123 Main St",
            phone="+1234567890",
            payment_method="Credit Card"
        )
        self.assertEqual(order.user_id, 12345)
        self.assertEqual(order.full_name, "John Doe")
        self.assertEqual(order.payment_method, "Credit Card")
        self.assertIsNotNone(order.created_at)

    def test_add_item_to_order(self):
        order = Order.objects.create(
            user_id=12345,
            full_name="John Doe",
            address="123 Main St",
            phone="+1234567890",
            payment_method="Credit Card"
        )
        order_item = OrderItem.objects.create(
            order=order,
            product=self.product,
            quantity=2,
            price=Decimal('100.00')
        )
        self.assertEqual(order_item.order, order)
        self.assertEqual(order_item.product, self.product)
        self.assertEqual(order_item.quantity, 2)
        self.assertEqual(order_item.price, Decimal('100.00'))
        self.assertIn(order_item, order.items.all())
