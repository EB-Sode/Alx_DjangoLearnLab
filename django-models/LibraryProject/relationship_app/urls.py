from .views import list_books, LibraryDetailView, RegisterView, LoginView
from django.urls import path, include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')), # Includes default auth URLs like login, logout, password change, etc.
]