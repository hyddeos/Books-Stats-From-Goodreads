from django.shortcuts import render
from .utils import Run
from .models import Books
from . serializers import *
from rest_framework import generics

class ListBooks(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class DetailBooks(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

# Create your views here.
def index(request):

    newndata = False
    if newndata:
        Run()


    return render(request, 'books/index.html', {
        'books' : Books.objects.all
    }

    )

