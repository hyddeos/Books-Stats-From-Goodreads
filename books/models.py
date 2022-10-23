from turtle import title
from typing import Collection
from django.db import models




class Books(models.Model):
    goodreadsID = models.CharField(blank=True, max_length=256)
    title = models.CharField(blank=True, max_length=256)
    authorLF =  models.CharField(blank=True, max_length=256)
    authorFL = models.CharField(blank=True, max_length=256)
    ISBN = models.CharField(null=True, max_length=256)
    ISBN13 = models.CharField(blank=True, max_length=256)
    myRating = models.CharField(blank=True, max_length=256)
    avgRating = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    publisher = models.CharField(blank=True, max_length=256)
    pages = models.IntegerField(null=True)
    published = models.CharField(blank=True, max_length=256, default=0)
    firstpublished = models.CharField(blank=True, max_length=256, default=0)
    dateRead = models.CharField(blank=True, max_length=256)
    dateAdded = models.CharField(blank=True, max_length=256)
    bookShelves = models.CharField(blank=True, max_length=600)
    readStatus = models.CharField(blank=True, max_length=256)
    readCount = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.title}'



