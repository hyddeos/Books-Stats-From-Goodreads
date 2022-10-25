from urllib import request
from xmlrpc.client import ResponseError
from django.shortcuts import render
from .utils import Run, Years
from .models import Books
from django.db.models import Count

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
        print("CHECK:", Books.objects.filter(readStatus='read').count())
        readBooks = Books.objects.filter(readStatus='read').count()
        toRead = Books.objects.filter(readStatus='to-read').count()
        currentlyreading = Books.objects.filter(readStatus='currently-reading').count()
        years = Years()
    

        data =  {
            'readBooks' : str(readBooks),
            'toRead' : str(toRead),
            'currentlyReading' : str(currentlyreading)
        }
        return Response(data)
