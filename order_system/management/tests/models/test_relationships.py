from django.test import TestCase
from django.db.models.deletion import ProtectedError
from decimal import Decimal
from ...models import Category, Product, Cart, CartItem, Order, OrderItem


class ModelRelationshipsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Test Product",
            price=Decimal('100.00'),
            category=self.category
        )
        self.cart = Cart.objects.create(user_id=12345)
        self.order = Order.objects.create(
            user_id=12345,
            full_name="John Doe",
            address="123 Main St",
            phone="+1234567890",
            payment_method="Credit Card"
        )

    def test_cascade_delete_cart(self):
        cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=1
        )
        self.cart.delete()
        self.assertFalse(CartItem.objects.filter(id=cart_item.id).exists())

    def test_cascade_delete_order(self):
        order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1,
            price=Decimal('100.00')
        )
        self.order.delete()
        self.assertFalse(OrderItem.objects.filter(id=order_item.id).exists())

    def test_protect_product_in_order(self):
        OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1,
            price=Decimal('100.00')
        )
        with self.assertRaises(ProtectedError):
            self.product.delete()

    def test_protect_category_with_products(self):
        with self.assertRaises(ProtectedError):
            self.category.delete()

    def test_cascade_delete_empty_category(self):
        empty_category = Category.objects.create(name="Empty")
        subcategory = Category.objects.create(
            name="Subcategory",
            parent=empty_category
        )
        empty_category.delete()
        self.assertFalse(Category.objects.filter(id=subcategory.id).exists())
