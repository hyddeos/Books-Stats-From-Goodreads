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

    def years():
        # Before is everybook read before the logging started(preyears)
        beforeYear = 2017
        currentYear = datetime.now()
        preYear = Books.objects.filter(readStatus='read', dateRead__range=["1000-01-01", f"{beforeYear}-12-30"] ).count()

        # Loop through all years from after before year and to current year and add count to dict
        bookYears = {
            'preYear' : preYear,
        }     
        for bookYear in range(beforeYear+1, currentYear.year+1):
            bookYears['Year ' + str(bookYear)] = Books.objects.filter(readStatus='read', dateRead__range=[f"{bookYear}-01-01", f"{bookYear}-12-30"] ).count()

        return bookYears

    def categories():
        
        categories = {
            'Non-Fiction' : Books.objects.filter(readStatus='read', bookShelves='non-fiction').count(),
            'Philosophy' : Books.objects.filter(readStatus='read', bookShelves='philosophy-theology').count(),
            'Biography-Memoir' : Books.objects.filter(readStatus='read', bookShelves='biography-memoarer').count(),
            'Fiction' : Books.objects.filter(readStatus='read', bookShelves='fiction').count(),
            'Science-History' : Books.objects.filter(readStatus='read', bookShelves='science-history').count(),
        }
        return categories
        










