from django_filters import rest_framework as filters
from .models import Photo

class PhotoDateFilter(filters.FilterSet):
    date = filters.DateFilter(field_name="date", lookup_expr='date')

    class Meta:
        model = Photo
        fields = ['date']
