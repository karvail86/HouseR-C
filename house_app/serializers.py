from rest_framework import serializers
from .models import (UserProfile, Property, District, Review, City, Region, PropertyImage)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = ('username', 'email', 'password', 'first_name', 'last_name')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = UserProfile.objects.create_user(**validated_data)
    return user

  def to_representation(self, instance):
    refresh = RefreshToken.for_user(instance)
    return {
      'user': {
        'username': instance.username,
        'email': instance.email,
      },
      'access': str(refresh.access_token),
      'refresh': str(refresh),
    }


class UserLoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField(write_only=True)

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Неверные учетные данные")

  def to_representation(self, instance):
    refresh = RefreshToken.for_user(instance)
    return {
      'user': {
        'username': instance.username,
        'email': instance.email,
      },
      'access': str(refresh.access_token),
      'refresh': str(refresh),
    }

class UserProfileListSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = ['username', 'email', 'password']


class UserProfileDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = '__all__'

class PropertyCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Property
    fields = '__all__'

class UserProfileNameSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = ['username']


class DistrictSerializer(serializers.ModelSerializer):
  class Meta:
    model = District
    fields = ['district_name']

class DistrictListSerializer(serializers.ModelSerializer):
  class Meta:
    model = District
    fields = ['id','district_name']



class ReviewCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
  class Meta:
    model = City
    fields = ['city_name']

class CityListSerializer(serializers.ModelSerializer):
  class Meta:
    model = City
    fields = ['id','city_name']

class CityDetailSerializer(serializers.ModelSerializer):
  district_city = DistrictListSerializer(many=True,read_only=True)
  class Meta:
    model = City
    fields = ['city_name','district_city']

class RegionListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Region
    fields = ['id','region_name']

class RegionDetailSerializer(serializers.ModelSerializer):
  city_region = CityListSerializer(many=True,read_only=True)
  class Meta:
    model = Region
    fields = ['region_name','city_region']

class RegionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Region
    fields = ['region_name']

class PropertyImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image']

class PropertyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'title', 'price', 'property_type', 'property_stars']


class DistrictDetailSerializer(serializers.ModelSerializer):
  property_place = PropertyListSerializer(many=True, read_only=True)
  class Meta:
    model = District
    fields = ['district_name','property_place']

class PropertyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
  created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%H')
  buyer = UserProfileNameSerializer()

  class Meta:
    model = Review
    fields = ['buyer', 'comment', 'rating', 'created_date']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'



