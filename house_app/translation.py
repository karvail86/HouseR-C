from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('property_name',)

@register(PropertyImage)
class PropertyImageTranslationOptions(TranslationOptions):
    fields = ('property',)

@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('region_name',)

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)

@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ('district_name',)

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment', )