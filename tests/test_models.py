from django.test import TestCase

from restaurant.models import *

class MenuCase(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name='Ice Cream', price='4.99', inventory='20', item_description='Frozen creamy dessert')
        self.assertEqual(str(item), 'Ice Cream : 4.99')