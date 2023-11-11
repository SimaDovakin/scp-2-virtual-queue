from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Queue, Participant, Country, Region, City


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("id", "name")


class CountryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name",)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "name")


class RegionCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("name",)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name")


class CityCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("name",)


class QueueSerializer(serializers.ModelSerializer):
    creator = CreatorSerializer(read_only=True)

    class Meta:
        model = Queue
        fields = (
            "id",
            "creator",
            "name",
            "country",
            "region",
            "city",
            "address",
            "created_at",
        )


class QueueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = ("name", "country", "region", "city", "address")


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ("id", "user", "queue", "queue_order", "created_at")
