from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import ValidationError
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

# Create your views here.

#view for listing all books
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]


#view for retrieving a single book
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]

#view for creating a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  # Only logged-in users can create

    def perform_create(self, serializer):
        # Example: Prevent duplicate book titles for the same author
        title = self.request.data.get('title')
        author_id = self.request.data.get('author')
        
        if Book.objects.filter(title=title, author_id=author_id).exists():
            raise ValidationError({"error": "This author already has a book with that title."})
        

#update the a book list
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]  # Only logged-in users can update

    def perform_update(self, serializer):
        # Example: Prevent updating to a duplicate book title for the same author
        title = self.request.data.get('title')
        author_id = self.request.data.get('author')
        book_id = self.kwargs.get('pk')

        if Book.objects.filter(title=title, author_id=author_id).exclude(id=book_id).exists():
            raise ValidationError({"error": "This author already has a book with that title."})
        serializer.save()



#delete a book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  # Only logged-in users can delete
