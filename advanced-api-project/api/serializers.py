from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# The serialized models below
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        #include all the fields
        fields = '__all__'
    
    #validate the publication year to ensure the book is from the past
    def validate(self, data):

        current_year = datetime.now().year

        if data['publication_year'] > current_year:
            raise serializers.ValidationError('Choose a year from the past')
        return data

class AuthorSerializer(serializers.ModelSerializer):

    '''Serializing the books dynamically with the author'''
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name']