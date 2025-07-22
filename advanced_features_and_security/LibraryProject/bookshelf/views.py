from django.shortcuts import redirect, render, get_object_or_404
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@permission_required('bookshelf.can_view_books')
def book_list(request):
    books= Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

@permission_required('bookshelf.can_create_books', raise_exception= True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        if title and author:
            Book.objects.create(title=title, author=author)
            return redirect('list_books')  # Adjust to your book list view name
        else:
            error = "Both title and author are required."
            return render(request, 'relationship_app/add_book.html', {'error': error})
    return render(request, 'relationship_app/add_book.html')

@permission_required('bookshelf.can_edit_books', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        if title and author:
            book.title = title
            book.author = author
            book.save()
            return redirect('list_books')
        else:
            error = "Both title and author are required."
            return render(request, 'relationship_app/add_book.html', {'error': error})
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete_books')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})


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
            return redirect('bookshelf:list_books')  # Redirect to the book list after registration
    else:
        form = UserCreationForm()
    return render(request, 'bookshelf/register.html', {'form': form})

def is_admin(user):
    return user.role == 'Admin'

def is_librarian(user):
    return user.role == 'Librarian'

def is_member(user):
    return user.role == 'Member'

# def check_user_role(role):
#     def inner(user):
#         return (user.is_authenticated 
#                 and hasattr(user, 'userprofile') 
#                 and user.userprofile.role == role)
#     return inner
# def check_user_role(role):
#     def inner(user):
#         return user.role == role
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

