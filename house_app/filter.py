from django_filters import FilterSet
from .models import Property

class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'title': ['exact', 'icontains'],
            'price': ['gt', 'lt'],
            'property_type': ['exact'],
            'property_stars': ['exact'],
            'is_active': ['exact'],
        }
