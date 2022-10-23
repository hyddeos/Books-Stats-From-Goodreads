from rest_framework import serializers
from .models import *

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
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
            'price',
        )
        model = Books