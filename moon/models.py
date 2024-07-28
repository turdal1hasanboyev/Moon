from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to="Avatars/", null=True, blank=True)
    bio = models.CharField(max_length=225, null=True, blank=True)
    work = models.CharField(max_length=225, null=True, blank=True)
    adress = models.CharField(max_length=225, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.username
    

class GetInTouch(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class AboutMoon(models.Model):
    about = models.CharField(max_length=225, null=True, blank=True)
    bio = models.CharField(max_length=225, null=True, blank=True)
    logo = models.ImageField(upload_to="Logos/", null=True, blank=True)
    harvesta = models.CharField(max_length=225, null=True, blank=True)
    harvesta_logo = models.ImageField(upload_to="Logos/", null=True, blank=True)
    units_of_cattle = models.CharField(max_length=225, null=True, blank=True)
    units_of_cattle_logo = models.ImageField(upload_to="Logos/", null=True, blank=True)
    farm = models.CharField(max_length=225, null=True, blank=True)
    farm_logo = models.ImageField(upload_to="Logos/", null=True, blank=True)
    units_of_technic = models.CharField(max_length=225, null=True, blank=True)
    units_of_technic_logo = models.ImageField(upload_to="Logos/", null=True, blank=True)

    def __str__(self):
        return self.about
    

class SpecialOffers(models.Model):
    special_offers = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(upload_to="SpecialOffers/", null=True, blank=True)
    description = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.special_offers
    

class Products(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(upload_to="Products/", null=True, blank=True)

    def __str__(self):
        return self.name
    