from .views import all_books, LibraryDetailView
from django.urls import path

urlpatterns = [
    path('books/', all_books, name='all_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library'),
]