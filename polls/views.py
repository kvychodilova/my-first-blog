from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Book,Category


def index(request):
    return HttpResponse("Ahoj")

def filter_books(request, categ_name):
    result = Book.objects.filter(category__name__startswith=categ_name)
    response = ",, ".join([x.title for x in result])
    return HttpResponse(response)