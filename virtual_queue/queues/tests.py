from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import (
    Queue,
    Location,
    Country,
    Region,
    City
)


class QueueViewTestCase(TestCase):

    def setUp(self):
        self.user_1 = User.objects.create(
            username='test_user_1',
            password='12345'
        )
        self.user_2 = User.objects.create(
            username='test_user_2',
            password='12345'
        )
        self.default_location = self.setup_default_location()

    def setup_default_location(self):
        country = Country.objects.create(
            name='Ukraine'
        )
        region = Region.objects.create(
            name='Zhytomyr region'
        )
        city = City.objects.create(
            name='Zhytomyr'
        )
        location = Location.objects.create(
            country=country,
            region=region,
            city=city,
            address="Chudnivska street, 105, 10001"
        )

        return location

    def test_dashboard(self):

        queues = []
        for i in range(3):
            queue = Queue(
                creator=self.user_1,
                location=self.default_location,
                name=f"Test queue {i}"
            )
            queues.append(queue)

        for i in range(3):
            queue = Queue(
                creator=self.user_2,
                location=self.default_location,
                name=f"Test queue {i}"
            )
            queues.append(queue)

        Queue.objects.bulk_create(queues)

        url = reverse('queues:dashboard')

        response = self.client.get(url)

        all_queues = Queue.objects.order_by('-created_at')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['all_queues']), list(all_queues))
