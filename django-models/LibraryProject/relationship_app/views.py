from django.shortcuts import render
from .models import Library, Book
from django.views.generic import DetailView

# Create your views here.

def all_books(request):
    books= Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'