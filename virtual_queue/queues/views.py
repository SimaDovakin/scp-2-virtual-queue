from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import (
    CityCreateUpdateSerializer,
    QueueSerializer,
    QueueCreateSerializer,
    CountrySerializer,
    CountryCreateUpdateSerializer,
    RegionSerializer,
    RegionCreateUpdateSerializer,
    CitySerializer,
)

from queues.models import Queue, Country, Region, City


class QueueViewSet(viewsets.GenericViewSet):
    def get_queryset(self):
        return Queue.objects.select_related("creator").order_by("-created_at")

    @swagger_auto_schema(responses={200: QueueSerializer(many=True)})
    def list(self, request):
        serializer = QueueSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: QueueSerializer})
    def retrieve(self, request, pk=None):
        queue = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = QueueSerializer(queue)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=QueueCreateSerializer, responses={201: QueueSerializer}
    )
    def create(self, request):
        serializer = QueueCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        queue = serializer.save(creator=request.user)
        response_serializer = QueueSerializer(queue)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class CountryViewSet(viewsets.GenericViewSet):
    serializer_class = CountrySerializer

    def get_queryset(self):
        return Country.objects.order_by("name")

    @swagger_auto_schema(responses={200: CountrySerializer(many=True)})
    def list(self, request):
        serializer = CountrySerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: CountrySerializer})
    def retrieve(self, request, pk=None):
        country = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CountryCreateUpdateSerializer, responses={201: CountrySerializer}
    )
    def create(self, request):
        serializer = CountryCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        country = serializer.save()
        response_serializer = CountrySerializer(country)

        return Response(response_serializer.data)

    @swagger_auto_schema(
        request_body=CountryCreateUpdateSerializer, responses={200: CountrySerializer}
    )
    def update(self, request, pk=None):
        country = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = CountryCreateUpdateSerializer(country, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_country = serializer.save()

        return Response(CountrySerializer(updated_country).data)

    def destroy(self, request, pk=None):
        country = get_object_or_404(self.get_queryset(), pk=pk)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegionViewSet(viewsets.GenericViewSet):
    serializer_class = RegionSerializer

    def get_queryset(self):
        return Region.objects.order_by("name")

    @swagger_auto_schema(responses={200: RegionSerializer(many=True)})
    def list(self, request):
        serializer = RegionSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: RegionSerializer})
    def retrieve(self, request, pk=None):
        region = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = RegionSerializer(region)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=RegionCreateUpdateSerializer, responses={201: RegionSerializer}
    )
    def create(self, request):
        serializer = RegionCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        region = serializer.save()
        response_serializer = RegionSerializer(region)
        return Response(response_serializer.data)

    @swagger_auto_schema(
        request_body=RegionCreateUpdateSerializer, responses={200: RegionSerializer}
    )
    def update(self, request, pk=None):
        region = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = RegionCreateUpdateSerializer(region, data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_region = serializer.save()
        response_serializer = RegionSerializer(updated_region)
        return Response(response_serializer.data)

    def destroy(self, request, pk=None):
        region = get_object_or_404(self.get_queryset(), pk=pk)
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CityViewSet(viewsets.GenericViewSet):
    serializer_class = CitySerializer

    def get_queryset(self):
        return City.objects.order_by("name")

    @swagger_auto_schema(responses={200: CitySerializer(many=True)})
    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data)

    @swagger_auto_schema(responses={200: CitySerializer})
    def retrieve(self, request, pk=None):
        city = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.serializer_class(city)

        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CityCreateUpdateSerializer, responses={201: CitySerializer}
    )
    def create(self, request):
        serializer = CityCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        city = serializer.save()
        response_serializer = self.serializer_class(city)

        return Response(response_serializer.data)

    @swagger_auto_schema(
        request_body=CityCreateUpdateSerializer, responses={200: CitySerializer}
    )
    def update(self, request, pk=None):
        city = get_object_or_404(self.get_queryset(), pk=pk)

        serializer = CityCreateUpdateSerializer(city, data=request.data)
        serializer.is_valid(raise_exception=True)

        updated_city = serializer.save()
        response_serializer = CitySerializer(updated_city)

        return Response(response_serializer.data)

    def destroy(self, request, pk=None):
        city = get_object_or_404(self.get_queryset(), pk=pk)
        city.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
