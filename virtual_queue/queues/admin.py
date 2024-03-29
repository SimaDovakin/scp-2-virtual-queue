from django.contrib import admin

from .models import (
    Queue,
    Participant,
    Country,
    Region,
    City
)


class QueueAdmin(admin.ModelAdmin):
    model = Queue


class ParticipantAdmin(admin.ModelAdmin):
    model = Participant


class CountryAdmin(admin.ModelAdmin):
    model = Country


class RegionAdmin(admin.ModelAdmin):
    model = Region


class CityAdmin(admin.ModelAdmin):
    model = City


admin.site.register(Queue, QueueAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
