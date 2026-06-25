from django.test import TestCase
from .models import Menu, Booking

class MenuModelTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_menu_str(self):
        item = Menu.objects.get(title="IceCream")
        self.assertEqual(str(item), "IceCream : 80.00")

class BookingModelTest(TestCase):
    def setUp(self):
        Booking.objects.create(
            name="John",
            no_of_guests=4,
            booking_date="2026-01-01T10:00:00Z"
        )

    def test_booking_str(self):
        booking = Booking.objects.get(name="John")
        self.assertEqual(str(booking), "John")