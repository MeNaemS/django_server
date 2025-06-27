from django.test import TestCase
from decimal import Decimal
from ...models import Category, Product, Cart, CartItem


class CartModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Test Product",
            price=Decimal('100.00'),
            category=self.category
        )

    def test_create_cart(self):
        cart = Cart.objects.create(user_id=12345)
        self.assertEqual(cart.user_id, 12345)
        self.assertIsNotNone(cart.created_at)

    def test_add_item_to_cart(self):
        cart = Cart.objects.create(user_id=12345)
        cart_item = CartItem.objects.create(
            cart=cart,
            product=self.product,
            quantity=2
        )
        self.assertEqual(cart_item.cart, cart)
        self.assertEqual(cart_item.product, self.product)
        self.assertEqual(cart_item.quantity, 2)
        self.assertIn(cart_item, cart.items.all())

    def test_cart_item_default_quantity(self):
        cart = Cart.objects.create(user_id=12345)
        cart_item = CartItem.objects.create(
            cart=cart,
            product=self.product
        )
        self.assertEqual(cart_item.quantity, 1)
