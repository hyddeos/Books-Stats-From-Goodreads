from rest_framework import serializers
from .models import *

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'goodreadsID',
            'title',
        )
        model = Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'updated',
            'goodreadsID',
            'title',
            'authorLF',
            'authorFL',
            'ISBN',
            'ISBN13',
            'myRating',
            'avgRating',
            'publisher',
            'pages',
            'published',
            'firstpublished',
            'dateRead',
            'dateAdded',
            'bookShelves',
            'readStatus',
            'readCount',
        )
        model = Books
