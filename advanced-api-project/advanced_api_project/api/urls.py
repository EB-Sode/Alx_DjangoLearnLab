from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

#routers for the CRUD operations on books
# router = DefaultRouter()
# router.register(r'books_all', BookViewSet, basename='books_all')

urlpatterns = [
    # path('', include(router.urls)),
    path('books/', ListView.as_view(), name='book-list'),
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),
    path('books/create/', CreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),
]
