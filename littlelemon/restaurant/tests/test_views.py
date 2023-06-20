from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')

        Menu(title="Cake", price=5, inventory=20).save()
        Menu(title="Pie", price=4, inventory=10).save()

    def test_get_all(self):
        response = self.client.get(self.list_url)
        # print(response.data)
        
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        # print(serializer.data)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)