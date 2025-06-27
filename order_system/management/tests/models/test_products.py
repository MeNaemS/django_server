from django.test import TestCase
from decimal import Decimal
from ...models import Category, Product


class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Electronics")
        self.assertEqual(category.name, "Electronics")
        self.assertIsNone(category.parent)
        self.assertEqual(str(category), "Electronics")

    def test_create_subcategory(self):
        parent = Category.objects.create(name="Electronics")
        child = Category.objects.create(name="Phones", parent=parent)
        self.assertEqual(child.parent, parent)
        self.assertIn(child, parent.subcategories.all())

    def test_category_hierarchy(self):
        electronics = Category.objects.create(name="Electronics")
        phones = Category.objects.create(name="Phones", parent=electronics)
        smartphones = Category.objects.create(name="Smartphones", parent=phones)
        
        self.assertEqual(smartphones.parent, phones)
        self.assertEqual(phones.parent, electronics)
        self.assertIsNone(electronics.parent)


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")

    def test_create_product(self):
        product = Product.objects.create(
            name="iPhone 15",
            description="Latest iPhone",
            price=Decimal('999.99'),
            category=self.category
        )
        self.assertEqual(product.name, "iPhone 15")
        self.assertEqual(product.price, Decimal('999.99'))
        self.assertEqual(product.category, self.category)
        self.assertEqual(str(product), "iPhone 15")

    def test_product_without_description(self):
        product = Product.objects.create(
            name="Test Product",
            price=Decimal('100.00'),
            category=self.category
        )
        self.assertEqual(product.description, "")

    def test_product_price_precision(self):
        product = Product.objects.create(
            name="Test Product",
            price=Decimal('123.45'),
            category=self.category
        )
        self.assertEqual(product.price, Decimal('123.45'))
