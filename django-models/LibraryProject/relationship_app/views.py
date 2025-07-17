from django.shortcuts import render
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def list_books(request):
    books= Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'

class LoginView(DjangoLoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('register')
    template_name = 'relationship_app/login.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')  # Redirect after successful registration

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Log the user in after registration
        return super().form_valid(form)