from django.shortcuts import render
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
def list_books(request):
    books= Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'

class LoginView(LoginView):
    form_class = LoginView.form_class
    success_url = reverse_lazy('list_books')
    template_name = 'relationship_app/login.html'