from calendar import month
from email.policy import default
from turtle import title
from typing import Collection
from django.db import models
from django.db.models import Count
from datetime import datetime
from django.db.models import F, Sum

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
            'Non-Fiction' : Books.objects.filter(readStatus='read', bookShelves__contains='non-fiction').count(),
            'Philosophy' : Books.objects.filter(readStatus='read', bookShelves__contains='philosophy-theology').count(),
            'Biography-Memoir' : Books.objects.filter(readStatus='read', bookShelves__contains='biography-memoarer').count(),
            'Fiction' : Books.objects.filter(readStatus='read', bookShelves__contains='fiction').exclude(bookShelves__contains='non-fiction').count(),
            'Science-History' : Books.objects.filter(readStatus='read', bookShelves__contains='science-history').count(),
        }
        return categories

    def months():

        startyear = 2018
        currentYear = datetime.now()
        monthsList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Oct', 'Nov', 'Dec']

        # Get Totalt month for all years added togather
        monthsTotalCount = {}
        for month in range(11):
            monthsTotalCount[monthsList[month]] = Books.objects.filter(readStatus='read', dateRead__month=month+1).count()

        # Get Books per/month every year
        booksEachMonth = {}
        for year in range(startyear, currentYear.year+1):
            booksEachMonth["year" + str(year)] = {}
            for month in range(11):
                booksEachMonth["year" + str(year)][monthsList[month]] = Books.objects.filter(readStatus='read',dateRead__year=year, dateRead__month=month+1).count()

        months = [monthsTotalCount, booksEachMonth]

        return months
    
    # Check if prices already has been added
    def priceCheck():
        totalPrice = Books.objects.filter(readStatus='read').aggregate(Sum('price'))['price__sum']
        return totalPrice










