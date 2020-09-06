from django.contrib.sites import requests
from django.db import models
from django.db.models import ManyToManyField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.db import models

from geoapp import settings


class Bookmark(models.Model):
    title = models.CharField(default='', blank=True, max_length=255)
    source_name = models.CharField(max_length=100)
    url = models.URLField('URL')


class Customer(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()


class CustomerBookmark(models.Model):
    enrolled_cust = models.ManyToManyField('Customer', blank=True)
    enrolled_book = models.ManyToManyField('Bookmark', blank=True)
