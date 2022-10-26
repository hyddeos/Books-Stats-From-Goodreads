from email.policy import default
from turtle import title
from typing import Collection
from django.db import models
from django.db.models import Count
from datetime import datetime

class Collection(models.Model):
    updated = models.DateTimeField(datetime.now(), default=None, null=True)

    def __str__(self):
        return f'ID:{self.id}'


class Books(models.Model):
    goodreadsID = models.IntegerField(null=True, default=0)
    title = models.CharField(blank=True, max_length=256)
    authorLF =  models.CharField(blank=True, max_length=256)
    authorFL = models.CharField(blank=True, max_length=256)
    ISBN = models.CharField(blank=True, max_length=256, default=0)
    ISBN13 = models.IntegerField(null=True, default=0)
    myRating = models.IntegerField(null=True, default=0)
    avgRating = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    publisher = models.CharField(blank=True, max_length=256)
    pages = models.IntegerField(null=True, default=0)
    published = models.CharField(blank=True, max_length=256, default=0)
    firstpublished = models.CharField(blank=True, max_length=256, default=0)
    dateRead = models.DateField(null=True, default=0)
    dateAdded = models.DateField(null=True, default=0)
    bookShelves = models.CharField(blank=True, max_length=600)
    readStatus = models.CharField(blank=True, max_length=256)
    readCount = models.IntegerField(null=True, default=0)
    price = models.DecimalField(blank=True, max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f'ID:{self.id} {self.title}'





