from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import BookSerializer
from rest_framework import generics, filters
from rest_framework.exceptions import ValidationError
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from django_filters import rest_framework

# Create your views here.
#class for case ignore while filtering
class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    author = django_filters.NumberFilter(field_name='author__id')
    publication_year = django_filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

#view for listing all books
class ListView(generics.ListAPIView):
    '''Api endpoint that allows books to be viewed, searched, filtered and ordered'''

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author']  # 'author__name' for related field search
    ordering_fields = ['title', 'publication_year']


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
