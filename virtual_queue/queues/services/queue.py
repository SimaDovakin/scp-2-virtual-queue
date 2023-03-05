from django.contrib.auth.models import User

from queues.models import Queue, Location


class QueueService:

    def create_queue(self, cleaned_form_data: dict, user: User) -> Queue:
        country = cleaned_form_data['country']
        region = cleaned_form_data['region']
        city = cleaned_form_data['city']
        address = cleaned_form_data['address']

        location = Location(
            country=country,
            region=region,
            city=city,
            address=address
        )
        location.save()

        queue_name = cleaned_form_data['name']

        queue = Queue(
            name=queue_name,
            location=location,
            creator=user
        )
        queue.save()

        return queue
