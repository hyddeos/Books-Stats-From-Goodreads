from turtle import title
from typing import Collection
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Books(models.Model):
    goodreadsID = models.BigAutoField(blank=True)
    title = models.CharField()
    authorLF =  models.CharField(blank=True)
    authorFL = models.CharField(blank=True)
    ISBN = models.BigAutoField(blank=True)
    ISBN13 = models.BigAutoField(blank=True)
    myRating = models.IntegerField(blank=True)
    avgRating = models.IntegerField(blank=True)
    publisher = models.CharField(blank=True)
    pages = models.IntegerField(blank=True)
    published = models.IntegerField(blank=True)
    firstpublished = models.IntegerField(blank=True)
    dateRead = models.CharField(blank=True)
    dateAdded = models.CharField(blank=True)
    readStatus = models.CharField(blank=True)
    readCount = models.IntegerField(blank=True)



