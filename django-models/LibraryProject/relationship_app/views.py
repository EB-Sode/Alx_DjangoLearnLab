from django.shortcuts import redirect, render
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def list_books(request):
    books= Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

class LoginView(DjangoLoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('register')
    template_name = 'relationship_app/login.html'

class LogoutView(auth_views.LogoutView):
    template_name = 'relationship_app/logout.html'


# class Register(CreateView):
#     form_class = UserCreationForm
#     template_name = 'relationship_app/register.html'
#     success_url = reverse_lazy('login')  # Redirect after successful registration

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)  # Log the user in after registration
#         return super().form_valid(form)
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('relationship_app:list_books')  # Redirect to the book list after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def is_admin(user):
    return hasattr(user, 'profile') and user.profile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'profile') and user.profile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'profile') and user.profile.role == 'Member'

# def check_user_role(role):
#     def inner(user):
#         return (user.is_authenticated 
#                 and hasattr(user, 'userprofile') 
#                 and user.userprofile.role == role)
#     return inner

# @user_passes_test(check_user_role('Admin'))
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# @user_passes_test(check_user_role('Librarian'))
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# @user_passes_test(check_user_role('Member'))
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')