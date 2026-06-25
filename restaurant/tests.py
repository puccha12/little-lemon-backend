from django.test import TestCase
from .models import Menu, Booking
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class MenuTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)

    def test_get_all_menu_items(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)

    def test_menu_str(self):
        item = Menu.objects.get(title="IceCream")
        self.assertEqual(str(item), "IceCream : 80.00")

class BookingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_booking(self):
        data = {
            'name': 'John',
            'no_of_guests': 4,
            'booking_date': '2026-01-01T10:00:00Z'
        }
        response = self.client.post(
            '/restaurant/booking/tables/', data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED)