from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Book

# The serialized models below

class BookSerializer (ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'