from django.db import models
from django.contrib.auth.models import User


class Queue(models.Model):
    """
    Stores the data of a particular queue.
    """
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='queues'
    )
    name = models.CharField(max_length=256)
    country = models.ForeignKey(
        'queues.Country', on_delete=models.CASCADE, related_name='queues'
    )
    region = models.ForeignKey(
        'queues.Region', on_delete=models.CASCADE, related_name='queues'
    )
    city = models.ForeignKey(
        'queues.City', on_delete=models.CASCADE, related_name='queues'
    )
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.creator_id})"


class Participant(models.Model):
    """
    Binds User and Queue models. Stores the order number of users in
    a particular queue.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participations')
    queue = models.ForeignKey(Queue, on_delete=models.CASCADE, related_name='participants')
    queue_order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.queue.name})"


class Country(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
