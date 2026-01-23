from django_filters import FilterSet
from .models import Property

class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'title': ['exact'],
            'price':['gt', 'lt'],
        }