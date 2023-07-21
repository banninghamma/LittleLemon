from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase, APIClient

from restaurant.views import *
from restaurant.serializers import MenuSerializer

client = APIClient()

class MenuViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('testadmin', 'testadmin@123!')
        client.force_login(self.user)
        Menu.objects.create(name='Cake', price='6.99', inventory=10, item_description='')
        Menu.objects.create(name='Ice Cream', price='4.99', inventory=20, item_description='')
        Menu.objects.create(name='Pie', price='5.99', inventory=5, item_description='')

    def test_get_menu(self):
        response = client.get(reverse('get_menu'))
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)