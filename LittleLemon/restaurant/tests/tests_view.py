from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .. models import Menu
from .. serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create some Menu objects for testing
        Menu.objects.create(title="Burger", price=5.99, inventory=100)
        Menu.objects.create(title="Fries", price=2.99, inventory=500)
        Menu.objects.create(title="Coke", price=1.99, inventory=200)

    def test_getall(self):
        # Make a GET request to retrieve all Menu objects
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)