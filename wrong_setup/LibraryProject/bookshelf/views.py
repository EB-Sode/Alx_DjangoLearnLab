from django.shortcuts import render
from .models import Book


# Create your views here.
book=Book.objects.get(author="George Orwell")
book.delete()