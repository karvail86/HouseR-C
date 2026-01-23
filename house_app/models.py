from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    password = models.CharField(max_length=40)
    RoleChoices = (
    ('seller','seller'),
    ('buyer','buyer'),
    )
    role_user = models.CharField(max_length=20, choices=RoleChoices, default='seller')
    registered_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Property(models.Model):
    property_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=100)
    property_stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    price = models.PositiveSmallIntegerField()
    date = models.DateField(auto_now_add=True)
    PropertyTypeChoices = (
    ('Квартиру','Квартиру'),
    ('Дом','Дом'),
    ('Коммерчесская недвижимость','Коммерчесская недвижимость'),
    ('Участок','Участок'),
    ('Дачу','Дачу'),
    ('Гараж','Гараж'),
    )
    property_type = models.CharField(max_length=30, choices=PropertyTypeChoices)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owner')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.property_name


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f'{self.property}, {self.image}'


class Region(models.Model):
    region_name = models.CharField(max_length=30)

    def __str__(self):
        return self.region_name


class City(models.Model):
    city_name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=50)

    def __str__(self):
        return self.district_name


class Review(models.Model):
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __int__(self):
        return self.buyer

