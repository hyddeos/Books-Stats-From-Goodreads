from turtle import update
from urllib import request
from xmlrpc.client import ResponseError
from django.shortcuts import render
from .utils import Run
from .models import Books
from django.db.models import Count
from django.db.models import F, Sum
from django.db.models import Avg

from . serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

class ListBooks(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class DetailBooks(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


# Create your views here.
def index(request):


    # Only loads new file if DB is empty
    if Books.objects.filter(readStatus='read').count() == 0:
      Run()

    return render(request, 'books/index.html', {
        'books' : Books.objects.all,
    }

    )

@api_view(['GET'])
def booksdata(request):
    if request.method == 'GET':

        # Total Books
        readBooks = Books.objects.filter(readStatus='read').count()
        toRead = Books.objects.filter(readStatus='to-read').count()
        currentlyreading = Books.objects.filter(readStatus='currently-reading').count()
        firstYear = Books.objects.filter(readStatus='read').exclude(dateRead="1000-01-01").order_by('dateRead')[:1][0].dateRead.year
        # Books Over the Years

        # Random Book Tips
        randomTipsData = Books.objects.filter(myRating=5).exclude(ISBN13__isnull=True).order_by('?')[:1][0]
        randomTips = {
            "title" : str(randomTipsData.title),
            "avgRating" : str(randomTipsData.avgRating),
            "dateRead" : randomTipsData.dateRead,
            "ISBN13" : str(randomTipsData.ISBN13)[:-1],
            "author" : randomTipsData.authorLF,
        }

        # Pages
        qualifiedBooks = Books.objects.filter(readStatus='read', pages__gte=30).count()
        avgPages = int(Books.objects.filter(readStatus='read', pages__gte=30).aggregate(Avg('pages'))['pages__avg'])
        booksWithOutPages = (readBooks - qualifiedBooks) * avgPages
        totalPages = Books.objects.filter(readStatus='read', pages__gte=30).aggregate(Sum('pages'))['pages__sum'] + booksWithOutPages
        print("tot avg : 312", readBooks)
        print("qualifiedBooks", qualifiedBooks)
        print("avgpages", (readBooks - qualifiedBooks) * avgPages)
        print("bwp", booksWithOutPages)
        print("TP", totalPages)

        print(randomTips)


        data =  {
            'readBooks' : str(readBooks),
            'toRead' : str(toRead),
            'currentlyReading' : str(currentlyreading),
            'firstYear' : str(firstYear),
            'randomTips' : dict(randomTips),
        }
        return Response(data)
