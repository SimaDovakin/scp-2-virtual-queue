from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r"queues", views.QueueViewSet, basename="queues")
router.register(r"countries", views.CountryViewSet, basename="countries")
router.register(r"regions", views.RegionViewSet, basename="regions")
router.register(r"cities", views.CityViewSet, basename="cities")

app_name = "queues"

urlpatterns = [
    path("", include(router.urls)),
]
