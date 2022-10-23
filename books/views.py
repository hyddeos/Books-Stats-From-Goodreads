from urllib import request
from xmlrpc.client import ResponseError
from django.shortcuts import render
from .utils import Run
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

    print("total", Books.totalBooks)
    # Change if you want to load a new file
    newndata = False
    if newndata:
        Run()

    return render(request, 'books/index.html', {
        'books' : Books.objects.all,
    }

    )

@api_view(['GET'])
def booksdata(request):
    if request.method == 'GET':

        readBooks = Books.objects.filter(readStatus='read').count()
        toRead = Books.objects.filter(readStatus='to-read').count()
    

        data =  {
            'readBooks' : str(readBooks),
            'toRead' : str(toRead),
        }
        return Response(data)
