from django.shortcuts import render
from .utils import Run
from .models import Books

# Create your views here.
def index(request):

    newndata = False
    if newndata:
        Run()


    return render(request, 'books/index.html', {
        'books' : Books.objects.all
    }

    )