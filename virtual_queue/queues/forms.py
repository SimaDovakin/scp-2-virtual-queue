from django import forms

from queues.models import (
    Country,
    City,
    Region
)


class QueueForm(forms.Form):
    name = forms.CharField(label='Queue name', max_length=256)
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        empty_label='Select country'
    )
    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        empty_label='Select region'
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        empty_label='Select city'
    )
    address = forms.CharField(
        label='Address',
        max_length=500
    )
